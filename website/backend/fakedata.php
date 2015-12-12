<?php 



require_once ('../inc/mysqlDb.php');
$db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

//$emptyTable = $db->rawQuery("DELETE * FROM balloon");

$fakedata = Array ("event_id" => "1",
               "timestamp" => "0000-00-00 00:00:00",
               "latitude" => rand(12, 57),
               "longitude" => rand(12, 57),
               "temperature" => rand(0, -57),
               "altitude" => rand(0, 30000),
               "humidity" => rand(0, 100),
               "image_url" => '/',
               "image" => '0'
);

$id = $db->insert ('balloon', $fakedata);
if($id)
    echo 'user was created. Id=' . $id;





?>