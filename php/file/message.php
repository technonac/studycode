<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guest Book</title>
</head>
<body>
<?php

$filename = "text_data.txt";

if (isset($_POST['sub'])) {
    $message = $_POST["username"] . "||" . $_POST["title"] . "||" . $_POST["mess"] . "<|>";
    writeMessage($filename, $message);
}

if (file_exists($filename)) {
    readMessage($filename);
}


function writeMessage($filename, $message)
{
    $fp = fopen($filename, 'a');
    if (flock($fp, LOCK_EX)) {
        fwrite($fp, $message);
        flock($fp, LOCK_UN);
    } else {
        echo "failed to lock file";
    }
    fclose($fp);
}

function readMessage($filename)
{
    $fp = fopen($filename, 'r');
    flock($fp, LOCK_SH);
    $buffer = "";
    while (!feof($fp)) {
        $buffer .= fread($fp, 1024);
    }
    $data = explode("<|>", $buffer);

    foreach ($data as $line) {
        list($username, $title, $message) = explode("||", $line);
        if ($username != "" && $title != "" && $message != "") {
            echo $username . "said: ";
            echo "&nbsp" . $title . " , ";
            echo $message . "<hr>";
        }
    }
    flock($fp, LOCK_UN);
    fclose($fp);
}

?>
<form action="" method="post">
    Username<input type="text" size="10" name="username"><br/>
    Title<input type="text" size="30" name="title"><br/><br/>
    <textarea name="mess" rows="4" cols="38">input something here...</textarea>
    <br/>
    <input type="submit" name="sub" value="submit">
</form>
</body>
</html>