<?php 

    require_once ('../inc/mysqlDb.php');
    $db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    
    $emptyTable = $db->rawQuery("TRUNCATE TABLE `car`");
    $emptyTable = $db->rawQuery("TRUNCATE TABLE `prediction`");
    $emptyTable = $db->rawQuery("TRUNCATE TABLE `balloon`");
    
    
?>