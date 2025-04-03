# Introduction
本项目存在的目的是为了同步代码，目前支持git的同步

支持 git ssh方式同步

支持 git http方式同步(需要账号密码)

推荐ssh方式,不推荐http方式

ssh更安全,支持lfs大文件,侵入低


# TODO
- [x] 单独设置ssh_key_path
- [x] 删掉name字段，采用public_repo的后缀name
- [ ] 拆分一个工具类出来，方便调用，main方法只保留核心代码
- [ ] 检测远程仓库是否存在
- [ ] 支持多仓库同步 
- [ ] 支持http的模式同步，账号密码写到仓库的信息中
- [ ] clone仓库时随机生成一个文件夹名称，作为clone路径，避免出现同名仓库覆盖现有文件的情况



# Requirements
- git (require) 自行安装
- ssh证书 (require,强烈建议新建证书) `ssh-keygen -t rsa -b 4096 -f ./transfer_rsa_key -C "xxx@qq.com"`
- git-lfs(存在大文件使用时，需要下载大文件)
- 请确保运行的机器能同时访问两个git托管平台
- 请确保ssh有权限读写仓库
- 注意,多仓库同步中,项目名不能有重复，否则会异常!!!!! 未来会增加单独路径的支持



# Usage
在各个仓库中加入ssh证书,并设置`repo_config.json`

```json
{
  "file_path": "/Users/wangjiahao/Downloads/sync-git/", // git clone 文件路径(填写本机的路径)
  "repositories": [ // 仓库信息
    {
      "branches": ["main","test"], // 分支,多个分支用逗号分隔
      "public_repo": "ssh://git@gitlab.remember5.top:2222/wangjiahao/sync-git.git", // 公共仓库地址
      "private_repo": "ssh://git@gitlab1.remember5.top:2222/sh-zhiyun/vue-cli-template.git", // 私有仓库地址
      "ssh_key_path": "/Users/wangjiahao/Downloads/transfer_rsa_key" // ssh证书路径
    }
  ]
}
```


支持加密的ssh证书密码设置，环境变量`SSH_KEY_PASSWORD`设置密码即可


# FAQ



# Contact Me

- GitHub: https://github.com/remember-5
- Email: [1332661444@qq.com](mailto:1332661444@qq.com)
