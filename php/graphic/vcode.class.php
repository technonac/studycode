<?php

class VCode
{
    private $width; //验证码图片宽度
    private $height; //验证码图片高度
    private $codeNum; //验证码字符个数
    private $disturbColorNum; //干扰元素数量
    private $checkCode; //验证码字符
    private $image; //验证码资源

    function __construct($width = 80, $height = 20, $codeNum = 4)
    {
        $this->width = $width;
        $this->height = $height;
        $this->codeNum = $codeNum;
        $number = floor($width * $height / 15);
        if ($number > (240 - $codeNum)) {
            $this->disturbColorNum = 240 - $codeNum;
        } else {
            $this->disturbColorNum = $number;
        }

        $this->checkCode = $this->createCheckCode();
    }

    function __toString()
    {
        $_SESSION['code'] = strtoupper($this->checkCode);
        $this->outImg();
        return '';
    }

    /**
     * 输出图像
     */
    private function outImg()
    {
        $this->getCreateImage();
        $this->setDisturbColor();
        $this->outputText();
        $this->outputImage();
    }


    /**
     * 创建图片资源，并初始化背景
     */
    private function getCreateImage()
    {
        $this->image = imagecreatetruecolor($this->width, $this->height);
        $backColor = imagecolorallocate($this->image, rand(225, 255), rand(225, 255), rand(225, 255));
        @imagefill($this->image, 0, 0, $backColor);
        $border = imagecolorallocate($this->image, 0, 0, 0);
        imagerectangle($this->image, 0, 0, $this->width - 1, $this->height - 1, $border);
    }


    /**
     * 随机生成用户指定个数的字符串，去掉了容易混淆的字符oOLlz和数字012
     */
    private function createCheckCode()
    {
        $code = "3456789abcdefghijkmnpqrstuvwxyABCDEFGHIJKMNPQRSTUVWXY";
        $ascii = "";
        for ($i = 0; $i < $this->codeNum; $i++) {
            $char = $code[rand(0, strlen($code) - 1)];
            $ascii .= $char;
        }
        return $ascii;
    }

    /**
     * 向图中输出不同颜色的点
     */
    private function setDisturbColor()
    {
        for ($i = 0; $i <= $this->disturbColorNum; $i++) {
            $color = imagecolorallocate($this->image, rand(0, 255), rand(0, 255), rand(0, 255));
            imagesetpixel($this->image, rand(1, $this->width - 2), rand(1, $this->height - 2), $color);
        }

        for ($i = 0; $i < 10; $i++) {
            $color = imagecolorallocate($this->image, rand(0, 255), rand(0, 255), rand(0, 255));
            imagearc($this->image, rand(-10, $this->width), rand(-10, $this->height), rand(30, 300), rand(20, 200), 55, 44, $color);
        }
    }

    /**
     * 随机颜色，随机拜访，随机字符串向图像中输出
     */
    private function outputText()
    {
        for ($i = 0; $i < $this->codeNum; $i++) {
            $fontcolor = imagecolorallocate($this->image, rand(0, 128), rand(0, 128), rand(0, 128));
            $fontsize = rand(3, 5);
            $x = floor($this->width / $this->codeNum) * $i + 3;
            $y = rand(0, $this->height - imagefontheight($fontsize));
            imagechar($this->image, $fontsize, $x, $y, $this->checkCode[$i], $fontcolor);
        }
    }

    /**
     * 自动检测GD支持的图像类型，并输出图像
     */
    private function outputImage()
    {
        /*        if (imagetypes() && IMG_GIF) {
                    header("Content-Type:image/gif");
                    imagegif($this->image);
                } else if (imagetypes() && IMG_JPG) {
                    header("Content-Type:image/jpeg");
                    imagejpeg($this->image);
                } else if (imagetypes() && IMG_PNG) {
                    header("Content-Type:image/png");
                    imagepng($this->image);
                } else {
                    die("不支持图片的创建!");
                }
        */
        header("Content-Type:image/png");
        imagepng($this->image);
    }

    function __destruct()
    {
        imagedestroy($this->image);
    }
}