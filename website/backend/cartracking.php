<?php

require_once ('../mysqldb.php');
$db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

$distance_diff = 0;

/*
 * Returns the distance in meters 
 */
function distance($lat1, $lon1, $lat2, $lon2) {
  $theta = $lon1 - $lon2;
  $dist = sin(deg2rad($lat1)) * sin(deg2rad($lat2)) +  cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * cos(deg2rad($theta));
  $dist = acos($dist);
  $dist = rad2deg($dist);
  $miles = $dist * 60 * 1.1515;  
  return $miles * 1.609344;
}


$latitude = 0;
$longitude = 0;

if (isset($_GET["eventid"])) {
    $eventid = htmlspecialchars($_GET["eventid"]);
}
if (isset($_GET["lat"])) {
    $latitude = htmlspecialchars($_GET["lat"]);
}
if (isset($_GET["longitude"])) {
    $longitude = htmlspecialchars($_GET["longitude"]);
}
if (isset($_GET["time"])) {
    $time = htmlspecialchars($_GET["time"]);
}
if (isset($_GET["android"])) {
    $android = htmlspecialchars($_GET["android"]);
}

$cols = Array ("id", "longitude", "latitude");

$db->where ('event_id', $eventid);
$db->orderBy("id","desc");

$lastCoordinate = $db->get ("car", Array (1, 1));
//echo "Last executed query was ". $db->getLastQuery();

if ($lastCoordinate != null) {
    $lastCoordinate[0]['latitude'];
    $lastCoordinate[0]['longitude'];
    $distance_diff = distance($lastCoordinate[0]['latitude'], $lastCoordinate[0]['longitude'], $latitude, $longitude);
}
//echo $distance_diff;

$data = Array ('event_id' => $eventid,
               'timestamp' => $db->now(),
               'latitude' =>  $latitude,
               'longitude'=> $longitude
);

// If distance is more than 50m then insert into DB, otherwise ignore GPS location.
if ($distance_diff > 50 || $lastCoordinate == null) {
    $id = $db->insert('car', $data);
    if ($id)
        echo 'car record was created. Id=' . $id;
    else
        echo 'insert failed: ' . $db->getLastError();
    
}

/*
$carItems = $db->get ("car", null, $cols);
if ($db->count > 0)
    foreach ($carItems as $caritem) { 
        echo "<pre>";
        print_r ($caritem);
        echo "</pre>";
    }
    
  */  
?>