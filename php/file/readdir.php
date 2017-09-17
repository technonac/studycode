<?php
/**
 * Created by PhpStorm.
 * User: nonac
 * Date: 2017/8/30
 * Time: 0:53
 */

$num = 0;
$dir_name = 'e:/';
$dir_handle = opendir($dir_name);
echo '<!DOCTYPE html><html>';
echo '<head><meta charset="utf-8" /></head>';
echo '<table border="0" align="center" width="1000" cellpadding="0" cellspacing="0">';
echo '<caption><h2> dir ' . $dir_name . ' content </h2></caption>';
echo '<tr align="left" bgcolor="#cccccc">';
echo '<th>file name</th><th>file size</th><th>file type</th><th>modify time</th></tr>';
while ($file = readdir($dir_handle)) {
    $dir_file = $dir_name . DIRECTORY_SEPARATOR . $file;

    $bg_color = $num++ % 2 == 0 ? '#fffff' : '#cccccc';
    echo "<tr bgcolor='$bg_color'>";
    echo "<td>$file</td>";
    echo '<td>' . filesize($dir_file) . '</td>';
    echo '<td>' . filetype($dir_file) . '</td>';
    echo '<td>' . date('Y/m/d', filemtime($dir_file)) . '</td>';
    echo '</tr>';
}
echo '</table>';
closedir($dir_handle);
echo 'total file count: ' . $num;
echo '</html>';