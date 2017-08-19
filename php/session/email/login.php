<?php
session_start();
require 'connect.inc.php';

//如果用户单击提交表单的事件则进行验证
if(isset($_POST['sub'])){
    var_dump($_POST);
    $stmt = $pdo->prepare("SELECT id,username FROM user WHERE username=? and userpwd=?");
    $stmt->execute(array($_POST['username'],/*md5($_POST['password'])*/$_POST['password']));
    if($stmt->rowCount() > 0){
        $_SESSION = $stmt->fetch(PDO::FETCH_ASSOC); //将用户信息全部注册到session中
        $_SESSION['isLogin'] = 1; //注册一个用来判断登录成功的变量
        header("Location:index.php");
    }else {
        echo '用户名或密码错误';
    }
}
?>
<html>
<head><title>邮件系统登录</title></head>
<body>
<h2>欢迎光临邮件系统</h2>
<form action="login.php" method="post">
    用户名<input type="text" id="username" name="username"/><br/>
    密码<input type="password" id="password" name="password"/><br/>
    <input type="submit" name="sub" value="登录"/>
</form>
</body>
</html>

