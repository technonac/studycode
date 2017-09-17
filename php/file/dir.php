<?php
/**
 * Created by PhpStorm.
 * User: nonac
 * Date: 2017/8/30
 * Time: 0:42
 */

$path = '../file/file.php';
//get file name
echo basename($path) . '<br/>';
echo basename($path, '.php') . '<br/>';

echo dirname($path) . '<br/>';

$path_parts = pathinfo($path);
var_dump($path_parts);
echo $path_parts['dirname'];
echo '<br/>';
echo 'disk_free_space = ' . disk_free_space('c:\\');
echo '<br/>';
echo 'disk_total_space = ' . disk_total_space('c:\\');
echo '<br/>';


function dirSize($directory)
{
    $dir_size = 0;

    if ($dir_handle = @opendir($directory)) {

        while ($filename = readdir($dir_handle)) {
            if ($filename != '.' && $filename != '..') {
                $sub_file = $directory . '/' . $filename;
                if (is_dir($sub_file)) {
                    $dir_size += dirSize($sub_file);
                } else if (is_file($sub_file)) {
                    $dir_size += filesize($sub_file);
                }

            }
        }
        closedir($dir_handle);
        return $dir_size;
    }
}

//$dir_size = dirSize('F:\workspaces');
//echo 'dir size = ' . $dir_size;


function delDir($directory)
{
    if (file_exists($directory)) {

        if ($dir_handle = @opendir($directory)) {
            while ($filename = readdir($dir_handle)) {
                if ($filename != '.' && $filename != '..') {
                    $sub_file = $directory . '/' . $filename;
                    if (is_dir($sub_file)) {
                        delDir($sub_file);
                    } else if (is_file($sub_file)) {
                        unlink($sub_file);
                    }

                }
            }
            closedir($dir_handle);
            rmdir($directory);
        }
    }
}

//delDir('abc');

function copyDir($dirSrc, $dirTo)
{
    if (is_file($dirTo)) {
        echo 'destination is file';
        return;
    }

    if (!file_exists($dirTo)) {
        mkdir($dirTo);
    }
    if ($dir_handle = @opendir($dirSrc)) {
        while ($filename = readdir($dir_handle)) {
            if ($filename != '.' && $filename != '..') {
                $subSrcFile = $dirSrc . '/' . $filename;
                $subToFile = $dirTo . '/' . $filename;
                if (is_dir($subSrcFile)) {
                    copyDir($subSrcFile, $subToFile);
                } else if (is_file($subSrcFile)) {
                    copy($subSrcFile, $subToFile);
                }

            }
        }
        closedir($dir_handle);
    }
}