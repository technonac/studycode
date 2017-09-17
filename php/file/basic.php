<?php
/**
 * Created by PhpStorm.
 * User: nonac
 * Date: 2017/9/2
 * Time: 15:03
 */

$file_name = "data.txt";
function write_by_fwrite($file_name)
{
    $handle = fopen($file_name, 'w') OR die("failed to open the file");

    for ($row = 0; $row < 10; $row++) {
        fputs($handle, "fputs" . $row . "\n");
        fwrite($handle, "fwrite" . $row . "\n");
    }
    fclose($handle);
}

//write_by_fwrite($file_name);


function write_once($file_name)
{
    $data = "";
    for ($row = 0; $row < 10; $row++) {
        $data .= "lines {$row} \n";
    }
    file_put_contents($file_name, $data);
}

//write_once("data1.txt");


function fread_file($file_name)
{
    $handle = fopen($file_name, 'r') OR die("failed to open the file");
    //$contents = fread($handle, 100);
    $contents = "";
    while (!feof($handle)) {
        $contents .= fread($handle, 1024);
    }
    fclose($handle);
    echo $contents;
}

//fread_file($file_name);
//read file once
echo file_get_contents($file_name);
echo "<br />";

print_r(file($file_name));

readfile($file_name);