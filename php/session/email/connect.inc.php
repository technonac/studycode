<?php
/**
 * 数据库链接配置
 */
define("DSN", "mysql:host=localhost;dbname=testmail");
define("DBUSER", "root");
define("DBPASS", "root");

try{
    $pdo = new PDO(DSN, DBUSER, DBPASS);
}catch (PDOException $e){
    die('连接失败 :' . $e ->getMessage());
}
