<?php
  require_once ('../inc/mysqlDb.php');
    $db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    $data = $_POST;
    $data .= "hoi";
    $file = "image.data2";
    file_put_contents($file, $data);

?>