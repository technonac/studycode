<?php

$image = imagecreate(150, 150);

$bg = imagecolorallocate($image, 255, 255, 255);
$black = imagecolorallocate($image, 0, 0, 0);

$string = "IMAGETEXTTEXT";

imagestring($image, 3, 28, 70, $string, $black);
imagestringup($image, 3, 59, 115, $string, $black);

for ($i = 0, $j = strlen($string); $i < strlen($string); $i++, $j--) {
    imagechar($image, 3, 10 * ($i + 1), 10 * ($i + 2), $string[$i], $black);
    imagecharup($image, 3, 10 * ($i + 1), 10 * ($j + 2), $string[$i], $black);
}

header("Content-Type:image/png");
imagepng($image);
imagedestroy($image);