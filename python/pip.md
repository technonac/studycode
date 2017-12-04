pip是python的包管理工具

#安装包
pip install packageName

#升级pip
pip install --upgrade pip

#查看已安装的包
pip list

#显示当前安装的包及版本号
pip freeze

#将pip freeze命令的结果重定向到requirements.txt文件中
pip freeze > requirements.txt

#使用已有的requirements.txt文件在另一个环境上安装各种包
pip install -r requirements.txt

#查看包的详情
pip show packageName

#查看过期的包
pip list --outdated

#卸载包
pip uninstall packageName

#升级包
pip install packageName --upgrade

#显示包所在目录
pip show -f packageName

#搜索包
pip search keyword

#查询可升级的包
pip list -o

#下载包但不安装
pip install 包名 -d 目录

#打包
pip wheel 包名

