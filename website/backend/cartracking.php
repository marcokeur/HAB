<?php

echo "test";
$file = 'hab.cardata.log';

//$id = htmlspecialchars($_GET["id"]);
$latitude = htmlspecialchars($_GET["lat"]);
$longitude = htmlspecialchars($_GET["longitude"]);
$time = htmlspecialchars($_GET["time"]);
$android = htmlspecialchars($_GET["android"]);

$filecontents = implode(' ', array($latitude, $longitude, $time, $android));  
file_put_contents($file, $filecontents);

?>