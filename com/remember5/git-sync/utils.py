import os
import subprocess
import re
from typing import List, Dict, Any, Optional

def extract_repo_name(url: str) -> str:
    """从Git仓库URL提取仓库名称"""
    clean_url = url.rstrip('/').replace('.git', '')
    if clean_url.startswith('ssh://'):
        parts = re.split(r'[:/]', clean_url)
        return parts[-1]
    elif '@' in clean_url and ':' in clean_url:
        return clean_url.split(':')[-1].split('/')[-1]
    else:
        return clean_url.split('/')[-1]

def get_default_ssh_key() -> Optional[str]:
    """获取默认SSH密钥路径"""
    default_path = os.path.expanduser("~/.ssh/id_rsa")
    return default_path if os.path.exists(default_path) else None

def get_domain_from_url(url: str) -> str:
    """从URL中提取域名"""
    if url.startswith(('http://', 'https://')):
        match = re.match(r'https?://([^/]+)', url)
        return match.group(1) if match else ''
    elif url.startswith('git@') or url.startswith('ssh://'):
        if url.startswith('ssh://'):
            parts = url.split('@')[1].split('/')[0]
        else:
            parts = url.split('@')[1].split(':')[0]
        return parts.split(':')[0]  # 处理可能包含端口号的情况
    return ''

def get_auth_config(url: str, config: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """获取URL对应的认证配置"""
    domain = get_domain_from_url(url)
    if domain and 'auth_configs' in config:
        return config['auth_configs'].get(domain)
    return None

def run_git_command(args: List[str], error_msg: str, config: Dict[str, Any] = None, url: str = None) -> bool:
    """执行Git命令"""
    original_env = os.environ.copy()
    try:
        if config and url:
            auth_config = get_auth_config(url, config)
            if auth_config:
                auth_type = auth_config.get('type')
                
                # 处理SSH认证
                if auth_type == 'ssh' and url.startswith(('ssh://', 'git@')):
                    key_path = auth_config.get('key_path')
                    ssh_password = auth_config.get('password', '')
                    
                    if key_path and os.path.exists(key_path):
                        ssh_command = f'ssh -i {key_path} -o StrictHostKeyChecking=no'
                        
                        # 如果提供了SSH密钥密码，使用sshpass处理密码
                        if ssh_password:
                            # 设置环境变量，避免命令行中出现明文密码
                            os.environ['SSHPASS'] = ssh_password
                            ssh_command = f'sshpass -e {ssh_command}'
                        
                        os.environ['GIT_SSH_COMMAND'] = ssh_command
                
                # 处理HTTP认证
                elif auth_type == 'http' and url.startswith(('http://', 'https://')):
                    username = auth_config.get('username')
                    password = auth_config.get('password')
                    if username and password:
                        domain = get_domain_from_url(url)
                        # 配置Git凭证
                        subprocess.run(['git', 'config', '--global', f'credential.{domain}.username', username])
                        subprocess.run(['git', 'config', '--global', f'credential.{domain}.helper', 'store'])
                        # 存储凭证
                        credential = f'protocol=https\nhost={domain}\nusername={username}\npassword={password}\n'
                        subprocess.run(['git', 'credential-store', 'store'], input=credential, text=True)

        result = subprocess.run(args, check=True, capture_output=True, text=True)
        print(f"✅ {error_msg}成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {error_msg}失败: {e.stderr}")
        return False
    finally:
        # 恢复原始环境变量
        os.environ.clear()
        os.environ.update(original_env)

def clone_repository(repo: Dict[str, Any], config: Dict[str, Any]) -> None:
    """克隆源仓库"""
    repo_name = extract_repo_name(repo["source_repo"])
    repo_dir = os.path.join(config['file_path'], repo_name)

    if os.path.exists(repo_dir):
        print(f"⏭️ 仓库已存在，跳过: {repo_name}")
        return

    print(f"📥 开始克隆仓库: {repo_name}")
    original_dir = os.getcwd()
    try:
        os.makedirs(config['file_path'], exist_ok=True)
        os.chdir(config['file_path'])
        
        # 只克隆第一个分支
        first_branch = repo["branches"][0]
        if not run_git_command(
            ["git", "clone", "-b", first_branch, repo["source_repo"]], 
            f"克隆分支 {first_branch}",
            config,
            repo["source_repo"]
        ):
            return
            
        # 切换到仓库目录
        os.chdir(repo_dir)
        
        # 对其他分支，创建本地跟踪分支
        for branch in repo["branches"][1:]:
            run_git_command(
                ["git", "checkout", "-b", branch, f"origin/{branch}"],
                f"创建分支 {branch}",
                config,
                repo["source_repo"]
            )
            
    finally:
        os.chdir(original_dir)

def check_remote_repo_exists(url: str, config: Dict[str, Any]) -> bool:
    """检查远程仓库是否存在"""
    try:
        # 使用 git ls-remote 检查仓库是否存在
        result = run_git_command(
            ["git", "ls-remote", url],
            "检查远程仓库",
            config,
            url
        )
        return result
    except Exception as e:
        print(f"❌ 检查远程仓库失败: {str(e)}")
        return False

def should_check_remote_repo(url: str, config: Dict[str, Any]) -> bool:
    """判断是否需要检查远程仓库"""
    # 获取全局配置
    check_remote = config.get('check_remote_repo', False)
    
    # 获取域名特定配置
    auth_config = get_auth_config(url, config)
    if auth_config and 'check_remote_repo' in auth_config:
        check_remote = auth_config['check_remote_repo']
    
    return check_remote

def sync_repository(repo: Dict[str, Any], config: Dict[str, Any]) -> None:
    """同步到多个目标仓库"""
    for branch in repo["branches"]:
        print(f"\n🌿 正在同步分支: {branch}")

        # 切换分支
        if not run_git_command(
            ["git", "checkout", branch], 
            f"切换到分支 {branch}", 
            config,
            repo["source_repo"]
        ):
            continue

        # 拉取更新
        if not run_git_command(
            ["git", "pull", "origin", branch], 
            f"拉取分支 {branch}", 
            config,
            repo["source_repo"]
        ):
            continue

        # 推送到所有目标仓库
        for target_repo in repo["target_repos"]:
            # 根据配置决定是否检查远程仓库
            if should_check_remote_repo(target_repo, config):
                print(f"\n📤 正在检查目标仓库: {target_repo}")
                if not check_remote_repo_exists(target_repo, config):
                    print(f"❌ 目标仓库不存在或无法访问: {target_repo}")
                    continue
            
            print(f"📤 正在推送到目标仓库: {target_repo}")
            run_git_command(
                ["git", "push", "-f", target_repo, f"{branch}:{branch}"],
                f"推送到目标仓库 {target_repo} 分支 {branch}",
                config,
                target_repo
            ) 