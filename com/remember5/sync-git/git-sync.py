import os
import re
import json
import subprocess
import getpass
from typing import Optional, Dict, Any, List

def extract_repo_name(url: str) -> str:
    """从Git仓库URL提取仓库名称"""
    # 统一处理.git结尾
    clean_url = url.rstrip('/').replace('.git', '')

    # 处理不同协议格式
    if clean_url.startswith('ssh://'):
        # ssh://git@host:port/path/to/repo
        parts = re.split(r'[:/]', clean_url)
        return parts[-1]
    elif '@' in clean_url and ':' in clean_url:
        # git@host:path/to/repo
        return clean_url.split(':')[-1].split('/')[-1]
    else:
        # http/https 或其他协议
        return clean_url.split('/')[-1]

def load_config() -> tuple[str, List[Dict[str, Any]]]:
    """加载配置文件并验证必要字段"""
    try:
        with open('repo_config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)

            # 验证仓库配置
            for repo in config['repositories']:
                if 'public_repo' not in repo:
                    raise ValueError("缺少必要字段: public_repo")
                if 'private_repo' not in repo:
                    raise ValueError("缺少必要字段: private_repo")

            return config['file_path'], config['repositories']
    except Exception as e:
        raise Exception(f"加载配置文件失败: {str(e)}")

def get_default_ssh_key() -> Optional[str]:
    """获取系统默认的SSH密钥路径"""
    default_path = os.path.expanduser("~/.ssh/id_rsa")
    return default_path if os.path.exists(default_path) else None

def run_command(args: List[str], errmsg: str, ssh_key_path: Optional[str] = None) -> bool:
    """执行命令并处理异常"""
    original_ssh_command = os.environ.get('GIT_SSH_COMMAND', '')

    try:
        if ssh_key_path and os.path.exists(ssh_key_path):
            os.environ['GIT_SSH_COMMAND'] = f'ssh -i {ssh_key_path} -o StrictHostKeyChecking=no'

        result = subprocess.run(
            args,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"{errmsg}\n错误详情: {str(e)}")
        print(f"命令输出: {e.stderr}")
        return False
    finally:
        os.environ['GIT_SSH_COMMAND'] = original_ssh_command

def get_ssh_password() -> Optional[str]:
    """获取 SSH 密钥密码"""
    try:
        return getpass.getpass('请输入 SSH 密钥密码 (如果没有设置密码请直接回车): ')
    except Exception as e:
        print(f"获取密码输入失败: {str(e)}")
        return None

def check_ssh_key_encrypted(key_path: str) -> bool:
    """检查 SSH 密钥是否加密"""
    try:
        with open(key_path, 'r') as f:
            content = f.read()
            return 'ENCRYPTED' in content
    except Exception as e:
        print(f"检查 SSH 密钥加密状态失败: {str(e)}")
        return False

def setup_ssh_agent_for_key(key_path: str) -> bool:
    """为指定密钥设置SSH Agent"""
    try:
        if not os.path.exists(key_path):
            print(f"SSH密钥文件不存在: {key_path}")
            return False

        if check_ssh_key_encrypted(key_path):
            password = os.getenv('SSH_KEY_PASSWORD') or get_ssh_password()
            if not password:
                print("未提供加密密钥的密码")
                return False

            command = f'ssh-add {key_path} <<< "{password}"'
            result = subprocess.run(
                command,
                shell=True,
                executable='/bin/bash',
                capture_output=True,
                text=True
            )
        else:
            result = subprocess.run(
                ['ssh-add', key_path],
                capture_output=True,
                text=True
            )

        if result.returncode == 0:
            print(f"成功添加SSH密钥: {key_path}")
            return True

        print(f"添加SSH密钥失败: {result.stderr}")
        return False
    except Exception as e:
        print(f"SSH密钥处理失败: {str(e)}")
        return False

def check_and_clone(file_path: str, repositories: List[Dict[str, Any]]) -> None:
    """检查并克隆仓库"""
    for repo_item in repositories:
        repo_name = extract_repo_name(repo_item["public_repo"])
        full_repo_path = os.path.join(file_path, repo_name)
        if not os.path.exists(full_repo_path):
            git_clone(file_path, repo_item)
        else:
            print(f"仓库已存在，跳过克隆: {repo_name}")

def branch_exists(repo_url: str, branch: str, key_path: Optional[str]) -> bool:
    """检查分支是否存在于远程仓库"""
    try:
        original_ssh_command = os.environ.get('GIT_SSH_COMMAND', '')
        if key_path and os.path.exists(key_path):
            os.environ['GIT_SSH_COMMAND'] = f'ssh -i {key_path} -o StrictHostKeyChecking=no'

        result = subprocess.run(
            ["git", "ls-remote", "--heads", repo_url, branch],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        return result.returncode == 0 and f"refs/heads/{branch}" in result.stdout
    except Exception as e:
        print(f"检查分支时发生错误: {str(e)}")
        return False
    finally:
        os.environ['GIT_SSH_COMMAND'] = original_ssh_command

def git_clone(file_path: str, repo_item: Dict[str, Any]) -> None:
    """克隆git仓库（改进版）"""
    original_dir = os.getcwd()
    try:
        repo_name = extract_repo_name(repo_item["public_repo"])
        repo_dir = os.path.join(file_path, repo_name)
        os.makedirs(file_path, exist_ok=True)
        os.chdir(file_path)

        key_path = repo_item.get('ssh_key_path') or get_default_ssh_key()

        if not repo_item.get("branches"):
            print(f"仓库 {repo_name} 未指定需要迁移的分支")
            return

        first_branch = repo_item["branches"][0]
        if not branch_exists(repo_item["public_repo"], first_branch, key_path):
            print(f"初始分支 {first_branch} 不存在，跳过仓库克隆")
            return

        print(f"正在克隆初始分支: {first_branch}")
        success = run_command(
            ["git", "clone", "-b", first_branch, repo_item["public_repo"]],
            f"克隆初始分支 {first_branch} 失败",
            key_path
        )

        if not success:
            return

        os.chdir(repo_dir)
        for branch in repo_item["branches"][1:]:
            if branch_exists(repo_item["public_repo"], branch, key_path):
                print(f"正在创建本地分支: {branch}")
                run_command(
                    ["git", "checkout", "--track", f"origin/{branch}"],
                    f"创建跟踪分支 {branch} 失败",
                    key_path
                )
            else:
                print(f"分支 {branch} 不存在，已跳过")

        print(f"✅ 成功初始化仓库: {repo_name}")

    finally:
        os.chdir(original_dir)

def check_and_sync(file_path: str, repositories: List[Dict[str, Any]]) -> None:
    """检测并同步任务"""
    for repo in repositories:
        repo_name = extract_repo_name(repo["public_repo"])
        full_repo_path = os.path.join(file_path, repo_name)
        try:
            if os.path.exists(full_repo_path):
                os.chdir(full_repo_path)
                git_sync(repo)
        except Exception as e:
            print(f"处理仓库 {repo_name} 时发生错误: {str(e)}")

def git_sync(repo: Dict[str, Any]) -> None:
    """同步git仓库（改进版）"""
    key_path = repo.get('ssh_key_path') or get_default_ssh_key()

    # 获取所有远程更新
    if not run_command(["git", "fetch", "--all"], "获取远程更新失败", key_path):
        return

    # 同步所有分支
    for branch in repo["branches"]:
        try:
            # 切换到分支
            if not run_command(["git", "checkout", branch], f"切换分支失败: {branch}", key_path):
                continue

            # 重置到远程状态
            if not run_command(["git", "reset", "--hard", f"origin/{branch}"], f"重置分支失败: {branch}", key_path):
                continue

            # 推送到目标仓库
            if run_command(
                    ["git", "push", "-f", repo["private_repo"], f"{branch}:{branch}"],
                    f"推送失败: {branch}",
                    key_path
            ):
                print(f"✅ 成功同步分支 {branch}")
        except Exception as e:
            print(f"❌ 同步分支 {branch} 失败: {str(e)}")

if __name__ == "__main__":
    try:
        file_path, repositories = load_config()

        for repo in repositories:
            repo_name = extract_repo_name(repo["public_repo"])
            key_path = repo.get('ssh_key_path') or get_default_ssh_key()
            if key_path:
                print(f"\n🔑 正在处理仓库 {repo_name} 的SSH密钥...")
                if not setup_ssh_agent_for_key(key_path):
                    raise Exception(f"无法加载SSH密钥: {key_path}")
            else:
                print(f"⚠️ 警告：仓库 {repo_name} 未配置SSH密钥且未找到默认密钥")

        # 执行克隆和同步
        print("\n🚀 开始克隆仓库...")
        check_and_clone(file_path, repositories)

        print("\n🔄 开始同步仓库...")
        check_and_sync(file_path, repositories)

        print("\n🎉 迁移完成！")
    except Exception as e:
        print(f"\n❌ 程序执行出错: {str(e)}")
        exit(1)
