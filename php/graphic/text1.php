<?php
$image = imagecreatetruecolor(400, 30);

$white = imagecolorallocate($image, 255, 255, 255);
$grey = imagecolorallocate($image, 128, 128, 128);
$black = imagecolorallocate($image, 0, 0, 0);

imagefilledrectangle($image, 0, 0, 399, 29, $white); //白色矩形作为白色背景

$text = iconv("utf-8", "utf-8", "哈哈哈哈23333qwerty");
$font = 'simhei.ttf';

imagettftext($image, 20, 0, 12, 21, $grey, $font, $text); //阴影
imagettftext($image, 20, 0, 10, 20, $black, $font, $text); //文字

header("Content-Type:image/png");
imagepng($image);
imagedestroy($image);


