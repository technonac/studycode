<?php
session_start();
if (isset($_POST['submit'])) {
    if (strtoupper(trim($_POST["code"])) == $_SESSION['code']) {
        echo '验证码输入成功<br>';
    } else {
        echo '<font color="red">验证码输入错误!</font><br>';
    }
}

?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Image</title>
    <script>
        function newgdcode(obj, url) {
            obj.src = url + '?nowtime=' + new Date().getTime();
        }
    </script>
</head>
<body>
<img src="gencode.php" alt="看不清楚，换一张" style="cursor: pointer;" onclick="javascript:newgdcode(this,this.src);">
<form action="imgcode.php" method="post">
    <input type="text" size="4" name="code">
    <input type="submit" name="submit" value="提交">
</form>
</body>
</html>
