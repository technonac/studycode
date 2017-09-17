<?php
/**
 * Created by PhpStorm.
 * User: nonac
 * Date: 2017/8/29
 * Time: 22:45
 */
echo filetype('C:\Windows\System32\drivers\etc\hosts');
//clearstatcache();

function get_file_pro($file_name)
{
    if (!file_exists($file_name)) {
        echo 'destination file not exit <br/>';
        return;
    }

    if (is_file($file_name)) {
        echo $file_name . ' is a file <br/>';
    }

    if (is_dir($file_name)) {
        echo $file_name . ' is a directory<br/>';
    }

    echo 'file type : ' . get_file_type($file_name) . '<br/>';
    echo 'file size : ' . get_file_size(filesize($file_name)) . '<br/>';

    if (is_readable($file_name)) {
        echo 'file readable <br/>';
    }

    if (is_writable($file_name)) {
        echo 'file writable <br/>';
    }

    if (is_executable($file_name)) {
        echo 'file executable <br/>';
    }

    echo 'file create time :' . date('Y-m-d H:m:s', filectime($file_name)) . '<br/>';
    echo 'file last modify time :' . date('Y-m-d H:m:s', filemtime($file_name)) . '<br/>';
    echo 'file last open time :' . date('Y-m-d H:m:s', fileatime($file_name)) . '<br/>';
}

function get_file_type($file_name)
{
    $file_type = filetype($file_name);
    switch ($file_type) {
        case 'file':
            $type = 'normal file';
            break;
        case 'dir':
            $type = 'directory';
            break;
        case 'block':
            $type = 'block file';
            break;
        case 'char':
            $type = 'character devices file';
            break;
        case 'fifo':
            $type = 'named piped file';
            break;
        case 'link':
            $type = 'symbol link';
            break;
        case 'unknown':
            $type = 'unknown type';
            break;
        default:
            $type = 'unknown type';
    }
    return $type;
}

function get_file_size($bytes)
{
    if ($bytes >= pow(2, 40)) {
        $return = round($bytes / pow(1024, 4), 2);
        $suffix = 'TB';
    } elseif ($bytes >= pow(2, 30)) {
        $return = round($bytes / pow(1024, 3), 2);
        $suffix = 'GB';
    } elseif ($bytes >= pow(2, 20)) {
        $return = round($bytes / pow(1024, 2), 2);
        $suffix = 'MB';
    } elseif ($bytes >= pow(2, 10)) {
        $return = round($bytes / pow(1024, 1), 2);
        $suffix = 'KB';
    } else {
        $return = $bytes;
        $suffix = 'Byte';
    }
    return $return . ' ' . $suffix;
}


get_file_pro('file.php');


print_r(array_slice(stat('file.php'), 13));