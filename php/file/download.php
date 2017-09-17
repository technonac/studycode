<?php
$filename = "test.jpg";

header('Content-Type: image/jpeg');
header('Content-Disposition: attachment; filename="' . $filename . '"');
header('Content-Length: ' . filesize($filename));

readfile($filename);