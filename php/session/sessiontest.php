<?php

/**
 * session 使用cookie 本地会存储一个 SESSION_ID
 *
 * php.ini
 * session.name = PHPSESSID
 * session.save_path = /tmp
 * session.save_handler = files|user|sqlite|memcache
 *
 * session通过file保存时
 * filename: sess_vnhn34rmu5j37e7he77vhppvg7
 * format: 变量名|类型:长度:值;
 *
 */
session_start();
//
//$_SESSION['username'] = 'skysky';
//$_SESSION['uid'] = 1;

echo 'session id = ' . session_id();
/*
//session destory step
//1.开启session并初始化
session_start();

//2.删除所有session的变量，也可以用unset($_SESSION['variable'])逐个删除
$_SESSION = array(); //文件内容清空

//3.如果使用基于cookie的session。使用setcookie删除包含session id的cookie
if(isset($_COOKIE[session_name()])){
    setcookie(session_name(), '', time() - 3600, '/');
}

//4.最后彻底销毁sesiion
session_destroy(); //删除session文件
*/