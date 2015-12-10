<?php
    require_once ('../inc/mysqldb.php');
    $db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    
    // $data = $_POST; // TODO: Clean POST
    // $id = $db->insert('telemetry', $data);
    // if ($id)
    //     echo 'telemetry record was created. Id=' . $id;
    // else
    //     echo 'insert failed: ' . $db->getLastError();
?>

<!--
Telemetry data
Array (
    [timestamp] => 18-26-01
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