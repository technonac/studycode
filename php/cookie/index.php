<?php
if (!(isset($_COOKIE['isLogin']) && $_COOKIE['isLogin'] == '1')) {
    header("Location:login.php");
    exit();
}
?>

<html>
<head><title>home page</title></head>
<body>
<?php
echo 'hello' . $_COOKIE['username'];
?>
<a href="login.php?action=logout">Log out</a>
<p>hello world</p>
</body>
</html>
