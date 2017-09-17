<?php

/**
 * Class FileUpload
 * support multi upload
 */
class FileUpload
{
    private $path = "./uploads"; //上传文件保存的路径
    private $allowtype = array('jpg', 'gif', 'png'); //上传文件允许的类型
    private $maxsize = 1 * 1024 * 1024;  //1MB 上传文件的大小
    private $israndname = true; //是否随机命名

    private $originName;
    private $tmpFileName;
    private $fileType;
    private $fileSize;
    private $newFileName;
    private $errorCode = 0;
    private $errorMsg = "";

    /**
     * setting some upload param ,e.g. $path,$allowtype,$maxsize,$israndname
     * @param $key
     * @param $val
     * @return $this
     */
    public function set($key, $val)
    {
        $key = strtolower($key);
        if (array_key_exists($key, get_class_vars(get_class($this)))) {
            $this->setOption($key, $val);
        }
        return $this;
    }


    /**
     * Method to upload file
     * @param $fileField file field name of form
     * @return bool return true if upload success
     */
    public function upload($fileField)
    {
        $return = true;
        if (!$this->checkFilePath()) {
            $this->errorMsg = $this->getError();
            return false;
        }

        // 上传的文件信息
        $name = $_FILES[$fileField]['name']; //上传的文件原名称
        $tmp_name = $_FILES[$fileField]['tmp_name']; //临时文件地址
        $size = $_FILES[$fileField]['size'];
        $error = $_FILES[$fileField]['error'];

        if (is_array($name)) { //多文件上传
            $errors = array();

            //先检查错误
            for ($i = 0; $i < count($name); $i++) {
                if ($this->setFiles($name[$i], $tmp_name[$i], $size[$i], $error[$i])) {
                    if (!$this->checkFileSize() || !$this->checkFileType()) {
                        $errors[] = $this->getError();
                        $return = false;
                    }
                } else {
                    $errors[] = $this->getError();
                    $return = false;
                }
                //如果有问题，则重新初始化属性
                if (!$return) {
                    $this->setFiles();
                }
            }

            if ($return) {
                $fileNames = array();
                for ($i = 0; $i < count($name); $i++) {
                    if ($this->setFiles($name[$i], $tmp_name[$i], $size[$i], $error[$i])) {
                        $this->setNewFileName();
                        if (!$this->copyFile()) {
                            $errors[] = $this->getError();
                            $return = false;
                        }
                        $fileNames[] = $this->newFileName;
                    }
                }
                $this->newFileName = $fileNames;
            }

            $this->errorMsg = $errors;
            return $return;

        } else { // 单文件上传
            if ($this->setFiles($name, $tmp_name, $size, $error)) {
                if ($this->checkFileSize() && $this->checkFileType()) {
                    $this->setNewFileName();
                    if ($this->copyFile()) {
                        return true;
                    } else {
                        $return = false;
                    }
                } else {
                    $return = false;
                }
            }
            if (!$return) {
                $this->errorCode = $this->getError();
            }
            return $return;
        }


    }

    /**
     *  filename ,if multi upload return file name array
     * @return mixed
     */
    public function getFileName()
    {
        return $this->newFileName;
    }

    /**
     * if upload failed, call this method to get error message,if multi upload return array
     * @return string
     */
    public function getErrorMsg()
    {
        return $this->errorMsg;
    }

    private function getError()
    {
        $str = "upload file ({$this->originName}) failed : ";
        switch ($this->errorCode) {
            case 4:
                $str .= "no file uploaded";
                break;
            case 3:
                $str .= "only part of file uploaded";
                break;
            case 2:
                $str .= "upload file size exceed MAX_FILE_SIZE of form";
                break;
            case 1:
                $str .= "upload file size exceed value upload_max_filesize set in php.ini";
                break;
            case -1:
                $str .= "file type not allow";
                break;
            case -2:
                $str .= "upload file size can not exceed {$this->maxsize} Byte";
                break;
            case -3:
                $str .= "create upload folder failed ,please choose another upload path";
                break;
            case -4:
                $str .= "upload path must be set ";
                break;
            default:
                $str .= "unknown error";
                break;
        }
        return $str . "<br/>";
    }

    private function setFiles($name = "", $tmp_name = "", $size = 0, $error = 0)
    {
        $this->setOption('errorCode', $error);
        if ($error) {
            return false;
        }

        $this->setOption('originName', $name);
        $this->setOption('tmpFileName', $tmp_name);
        $aryStr = explode('.', $name);
        $this->setOption('fileType', strtolower($aryStr[count($aryStr) - 1]));
        $this->setOption('fileSize', $size);
        return true;
    }

    private function setOption($key, $val)
    {
        $this->$key = $val;
    }

    private function setNewFileName()
    {
        if ($this->israndname) {
            $this->setOption("newFileName", $this->getRandName());
        } else {
            $this->setOption("newFileName", $this->originName);
        }
    }

    private function checkFileType()
    {
        if (in_array(strtolower($this->fileType), $this->allowtype)) {
            return true;
        } else {
            $this->setOption('errorCode', -1);
            return false;
        }
    }

    private function checkFileSize()
    {
        if ($this->fileSize > $this->maxsize) {
            $this->setOption('errorCode', -2);
            return false;
        } else {
            return true;
        }
    }

    private function checkFilePath()
    {
        if (empty($this->path)) {
            $this->setOption('errorCode', -5);
            return false;
        }

        if (!file_exists($this->path) || !is_writable($this->path)) {
            if (!@mkdir($this->path, 0755)) {
                $this->setOption('errorCode', -4);
                return false;
            }

        }
        return true;
    }

    private function getRandName()
    {
        $fileName = date('YmdHis') . '_' . rand(100, 999);
        return $fileName . '.' . $this->fileType;
    }

    private function copyFile()
    {
        if (!$this->errorCode) {
            $path = rtrim($this->path, '/') . '/';
            $path .= $this->newFileName;
            if (@move_uploaded_file($this->tmpFileName, $path)) {
                return true;
            } else {
                $this->setOption('errorCode', -3);
                return false;

            }
        } else {
            return false;
        }
    }
}