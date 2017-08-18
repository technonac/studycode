<?php

function clearCookie()
{
    setcookie('username', '', time() - 3600);
    setcookie('isLogin', '', time() - 3600);
}

if (isset($_GET['action'])) {
    if ($_GET['action'] == 'login') {
        clearCookie(); //clear client cookie
        if ($_POST["user"] == "admin" && $_POST["password"] == "123456") {
            setcookie('username', $_POST['user'], time() + 60 * 60 * 24 * 7);
            setcookie('isLogin', '1', time() + 60 * 60 * 24 * 7);
            header("Location:index.php");
        } else {
            die('用户名或密码错误');
        }
    } else if ($_GET['action'] == 'logout') {
        clearCookie();
    }
}

?>
<html>
<head><title>用户登录</title></head>
<body>
<h2>用户登录</h2>
<?php var_dump($_POST) ?>
<form action="login.php?action=login" method="post">
    用户名<input type="text" id="user" name="user"/><br/>
    密码<input type="password" id="password" name="password"/><br/>
    <input type="submit" value="登录"/>
</form>
</body>
</html>
