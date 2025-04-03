import json
import os
import sys
from utils import extract_repo_name, clone_repository, sync_repository

def main():
    """主程序入口"""
    try:
        print("🚀 开始执行Git同步任务")

        # 加载配置
        print("⚙️ 正在加载配置文件...")
        with open('./repo_config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)

        # 处理每个仓库
        for repo in config['repositories']:
            try:
                repo_name = extract_repo_name(repo["source_repo"])
                print(f"\n📂 正在处理仓库: {repo_name}")

                # 克隆仓库
                clone_repository(repo, config)

                # 切换到仓库目录
                repo_dir = os.path.join(config['file_path'], repo_name)
                if os.path.exists(repo_dir):
                    os.chdir(repo_dir)
                    # 同步到所有目标仓库
                    sync_repository(repo, config)

            except Exception as e:
                print(f"❌ 处理仓库失败: {str(e)}")
                continue

        print("\n🎉 同步任务完成！")

    except Exception as e:
        print(f"❌ 程序执行出错: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
