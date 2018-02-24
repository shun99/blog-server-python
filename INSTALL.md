# 安装Python和虚拟环境(mac)
安装Python管理工具
```
brew install pyenv
//升级
brew upgrade pyenv
```
配置环境变量，在 ~/.bash_profile 中加入即可
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH=$PATH:/sbin/
eval "$(pyenv init -)"
```
安装Python
```
pyenv install 3.5.2
//查看版本
pyenv versions
```
切换Python版本
```
pyenv local 3.5.2
```
安装virtualenv
```
pip install virtualenv
//安装完成检测版本是否安装成功
virtualenv --version
```
创建虚拟环境
```
virtualenv env_name(环境名称)
```
激活虚拟环境
```
source env_name/bin/activate(activate路径)
```
激活之后命令行前带有项目名
```
//激活前
yghysdrdeMBP:blog-server-python yghysdr$
//激活后
(blog-server-python) yghysdrdeMBP:blog-server-python yghysdr$
```
退出虚拟环境
```
deactivate
```



