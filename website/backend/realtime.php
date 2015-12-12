<?php

    require_once ('../inc/mysqlDb.php');
    $db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Prepare array for the latest Car/Balloon data
    $data = array();
    
    $last_balloonId = 0;
    $last_carId = 0;


    if (isset($_GET["balloon_id"])) {
        $last_balloonId = htmlspecialchars($_GET["balloon_id"]);
    }

    if (isset($_GET["car_id"])) {
        $last_carId = htmlspecialchars($_GET["car_id"]);
    }
    
    //echo $last_carTimestamp;
    $db->where ('id', $last_carId, ">");
    $data['car'] = $db->get('car');
    //print_r($data['car']);
    
    $db->where ('id', $last_balloonId, ">");
    $data['balloon'] = $db->get('balloon');
    //print_r($data['balloon']);
    
    echo json_encode ($data);
?>