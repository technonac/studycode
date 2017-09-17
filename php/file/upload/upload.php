<?php

require 'fileupload.class.php'; //加载上传文件类

$up = new FileUpload();

$up->set('path', './uploads/')->set('size', 1000000)
    ->set('allowtype', array('jpg', 'png', 'gif'))
    ->set('israndname', true);

if ($up->upload('myfile')) {
    print_r($up->getFileName());
} else {
    print_r($up->getErrorMsg());
}
