1. 学习来源 youtube [py flask tutorial](https://youtu.be/V_3-e8AoIrE?feature=shared)
2. flask 框架、UV 管理虚拟环境

```
#uv 初始化命令
uv init
# uv 安装包
uv add flask
# uv 创建虚拟环境、进入、退出
uv venv --prompt flask
source .venv/Scripts/activate
deactivate

# 一个远程仓库、多个url
git remote add origin repourl1
git remote set-url --add origin  repourl2
```

3. 结构介绍

4. 时间线记录，算是 commit 的补充和学习总结
   1. 20250514：初学并练习到静态文件加载
   2. 20250517：新建测试数据库、指定 git 仓库
      1. 数据库在 7e 云主机；容器名 mariadb; 连接 host mariadb.chaoslong.cn ; 端口 3306

