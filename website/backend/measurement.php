<?php
   
    
    require_once ('../inc/mysqlDb.php');
    $db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    
    // Prepare array for the latest Car/Balloon data
    $data = array();
    $data['car'] = $db->get('car');
    $data['prediction'] = $db->get('prediction');
    
    $cols = Array ("id","event_id", "timestamp", "latitude", "longitude", "temperature", "altitude","humidity","has_image");
    
   
    $data['balloon'] = $db->get('balloon',null, $cols);

    echo json_encode ($data);
?>