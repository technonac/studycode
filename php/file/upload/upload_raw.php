<?php
/**
 * http://php.net/manual/zh/features.file-upload.php
 *
 *  Single file
 * array(1) { ["myfile"]=> array(5) {
 * ["name"]=> string(29) "photo_2017-09-12_14-29-47.jpg"
 * ["type"]=> string(10) "image/jpeg"
 * ["tmp_name"]=> string(45) "C:\Users\nonac\AppData\Local\Temp\phpC659.tmp"
 * ["error"]=> int(0)
 * ["size"]=> int(142253) }
 * }
 *
 * Multi file
 *array(1) { ["myfile"]=> array(5) {
 * ["name"]=> array(3) {
 * [0]=> string(29) "photo_2017-09-12_14-29-47.jpg"
 * [1]=> string(29) "photo_2017-09-12_14-29-48.jpg"
 * [2]=> string(0) "" }
 * ["type"]=> array(3) {
 * [0]=> string(10) "image/jpeg"
 * [1]=> string(10) "image/jpeg"
 * [2]=> string(0) "" }
 * ["tmp_name"]=> array(3) {
 * [0]=> string(45) "C:\Users\nonac\AppData\Local\Temp\php8977.tmp"
 * [1]=> string(45) "C:\Users\nonac\AppData\Local\Temp\php8978.tmp"
 * [2]=> string(0) "" }
 * ["error"]=> array(3) {
 * [0]=> int(0)
 * [1]=> int(0)
 * [2]=> int(4) }
 * ["size"]=> array(3) {
 * [0]=> int(142253)
 * [1]=> int(147059)
 * [2]=> int(0) } } }
 */

$upload_dir = "./uploads/";
if (!is_array($_FILES['myfile']['name'])) { //单文件上传
    $upload_file = $upload_dir . $_FILES['myfile']['name'];
    if (move_uploaded_file($_FILES['myfile']['tmp_name'], $upload_file)) {
        echo "File is valid, and was successfully uploaded.\n";
    } else {
        echo "Possible file upload attack!\n";
    }
} else { // 多文件上传
    foreach ($_FILES["myfile"]["error"] as $key => $error) {
        if ($error == UPLOAD_ERR_OK) {
            $tmp_name = $_FILES["myfile"]["tmp_name"][$key];
            $name = $_FILES["myfile"]["name"][$key];
            move_uploaded_file($tmp_name, $upload_dir . $name);
        }
    }
}
echo '<pre>';
print_r($_FILES);
print "</pre>";



