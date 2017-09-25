<?php
/**
 * 图片处理相关函数
 * imagecreatefromjpeg(); // 文件或者url创建一图像
 * imagecreatefrompng();
 * imagecreatefromgif();
 * getimagesize()
 */

/**
 * 向不同不同格式的图片中间 画一个字符串
 * @param $filename
 * @param $string
 */
function image($filename, $string)
{
    list($width, $height, $type) = getimagesize($filename);
    $types = array(1 => "gif", 2 => "jpeg", 3 => "gif");
    //不同类型调用不同的函数
    $createfrom = "imagecreatefrom" . $types[$type];
    $image = $createfrom($filename);
    $x = ($width - imagefontwidth(5) * strlen($string)) / 2;
    $y = ($height - imagefontheight(5)) / 2;
    $textcolor = imagecolorallocate($image, 255, 0, 0);
    imagestring($image, 5, $x, $y, $string, $textcolor);
    //图片输出函数
    $output = "image" . $types[$type];
    $output($image, "img_string." . $types[$type]);
    imagedestroy($image);
}

image("img.jpg", "HSHJSHJ");