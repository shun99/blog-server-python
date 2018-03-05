```
//安装
brew install mongodb
//创建
sudo mkdir -p /data/db
//三种方式启动
1. mongod --dbpath=/data/db 直接启动
2. mongod -f mongod.conf 通过配置文件启动
3. mongod --dbpath=/data/db --logpath=/data/log/example1.log --fork 使用Daemon启动
//进入mongodb的shell（在新窗口）
mongo
```