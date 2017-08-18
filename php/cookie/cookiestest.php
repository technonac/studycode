<?php

//set cookie
setcookie('username', 'hello', time() + 60 * 60 * 24 * 7, '/');

//delete cookie 1
//setcookie('username');
//delete cookie 2
//setcookie('username', '', time() - 1);

//set array cookie
setcookie("user[username]", 'sky');
setcookie("user[password]", md5("123456"));
setcookie("user[email]", "sky@sky.com");

foreach ($_COOKIE["user"] as $key => $value) {
    echo $key . ' : ' . $value . "\n";
}

//after refresh
var_dump($_COOKIE);
