<?php
session_start();
//从session中获取登录用户名
$username = $_SESSION['username'];

//删除所有session的变量
$_SESSION = array();

//判断是否使用基于cookie的session。使用setcookie删除包含session id的cookie
if(isset($_COOKIE[session_name()])){
    setcookie(session_name(), '', time() - 42000, '/');
}

//最后彻底销毁session
session_destroy();
?>
<html>
<head><title>退出系统</title></head>
<body>
   <p><?php echo $username ?> 再见!</p>
<p><a href="login.php">重新登录邮件系统</a> </p>
</body>
</html>

