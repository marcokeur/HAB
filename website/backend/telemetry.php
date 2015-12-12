<?php
    require_once ('../inc/mysqlDb.php');
    $db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    $data = $_POST;
    
    $data["event_id"] = 1;
    $data["has_image"] = false;
    $data["timestamp"] = date("Y-m-d H:i:s");
    $id = $db->insert('balloon', $data);
    if ($id)
        echo 'telemetry record was created. Id=' . $id ;
    else
        echo 'insert failed: ' . $db->getLastError();
?>

<!--
Telemetry data
Array (
    [timestamp_balloon] => 18-26-01
    [altitude] => 500
    [internal_temp] => 5.3
    [longitude] => 42.44431
    [humidity] => -30.0
    [sentence_id] => 0
    [callsign] => althab
    [air_pressure] => 40
    [external_temp] => 3.0
    [latitude] => 0.55444
)
-->