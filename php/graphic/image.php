<?php
/*
//图片大小
imagesx($image);
imagesy($image);
//画点线
imagesetpixel();
imageline();

//画矩形
imagerectangle();
imagefilledrectangle();

//画多边形
imagepolygon();
imagefilledpolygon();

//画椭圆
imageellipse();
imagefilledellipse();

//画圆弧
imagearc();
imagefilledarc();

//绘制文字
imagestring();
imagestringup();
imagechar();
imagecharup();
imagettftext();
*/
//创建画布，返回一个资源类型的变量，并在内存中开辟一块临时区域
$image = imagecreatetruecolor(100, 100); //创建画布 100x100
imageantialias($image, true); //抗锯齿

//设置图像中所需的颜色
$white = imagecolorallocate($image, 0xff, 0xff, 0xff);
$gray = imagecolorallocate($image, 0xc0, 0xc0, 0xc0);
$darkgray = imagecolorallocate($image, 0x90, 0x90, 0x90);
$navy = imagecolorallocate($image, 0x00, 0x00, 0x80);
$darknavy = imagecolorallocate($image, 0x00, 0x00, 0x50);
$red = imagecolorallocate($image, 0xff, 0x00, 0x00);
$darkred = imagecolorallocate($image, 0x90, 0x00, 0x00);


imagefill($image, 0, 0, $white); //背景色
//3d效果
for ($i = 60; $i > 50; $i--) {
    imagefilledarc($image, 50, $i, 100, 50, -160, 40, $darknavy, IMG_ARC_PIE);
    imagefilledarc($image, 50, $i, 100, 50, 40, 75, $darkgray, IMG_ARC_PIE);
    imagefilledarc($image, 50, $i, 100, 50, 75, 200, $darkred, IMG_ARC_PIE);
}
imagefilledarc($image, 50, 50, 100, 50, -160, 40, $navy, IMG_ARC_PIE);
imagefilledarc($image, 50, 50, 100, 50, 40, 75, $gray, IMG_ARC_PIE);
imagefilledarc($image, 50, 50, 100, 50, 75, 200, $red, IMG_ARC_PIE);

imagestring($image, 1, 15, 55, "34.7%", $white);
imagestring($image, 1, 45, 35, "55.5%", $white);


//像浏览器输出图片
header('Content-Type: image/png');
imagepng($image); //输出
imagedestroy($image);

