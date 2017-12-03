#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文件系统
os模块:常见的文件或目录操作函数
#文件处理
remove()/unlink():删除文件
rename()
stat() 返回文件信息
symlink()创建符号链接
utime()更新时间戳
tmpfile()创建并打开一个新的临时文件
walk()生成目录树下的所有文件名

#目录/文件夹
chdir()fchdir() 改变当前工作目录/通过一个文件描述符改变当前工作目录
chroot()改变当前进程的根目录
listdir()列出指定目录的文件
getcwd()/getcwdu() 返回当前工作目录
mkdir()/mkdirs()
rmdir()/rmdirs()

#访问/权限
aceess() 检验权限模式
chmod() 改变权限模式
chown() 改变owner/groupid
umask() 设置默认权限模式

#文件描述符操作
open() 底层操作系统open
read()/write()
dup()/dup2() 赋值文件描述符号

os.path模块: 针对路径名的操作
#分隔
basename():去掉目录庐江，返回文件名
dirname():去掉文件名，返回目录路径
join():将分离的各部分组合成一个路径名
split():返回(dirname(),basename())元组
splitdrive():返回(drivename,pathname)元组
splitext():返回(filename,extension)元组

#信息
getatime(): 最近访问时间
getctime(): 文件创建时间
getmtime():最近文件修改时间
getsize()： 文件大小 字节为单位

#查询
exits(): 指定路径是否存在
isabs(): 指定路径是否为绝对路径
isdir(): 指定路径是否存在且为一个目录
isfile():指定路径是否存在且为一个文件
islink():指定路径是否存在且为一个符号链接
ismount():指定路径是否存在且一个挂载点
samefile(): 两个路径名是否指向同一个文件

"""
