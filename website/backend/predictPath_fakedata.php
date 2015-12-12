<?php 
    // https://github.com/joshcam/PHP-MySQLi-Database-Class    


    //echo "disabled fake generation script! remove exit()";
    //exit();
    
    require_once ('../inc/mysqlDb.php');
    $db = new MysqliDb (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    
    $emptyTable = $db->rawQuery("TRUNCATE TABLE `car`");
    $emptyTable = $db->rawQuery("TRUNCATE TABLE `prediction`");
    $emptyTable = $db->rawQuery("TRUNCATE TABLE `balloon`");

    // Initial fake data paramters
    $fake_temperature = 20;
    $fake_altitude = 0;
    $fake_humidity = 60;
    
    //$fake_blob_image = file_get_contents("https://hab-henryfinlandia.c9users.io/website/img/highaltitude.jpg");
    
    $count = 0;
    
    $url = "http://predict.habhub.org/preds/9f56d7d6649c1cdb5902d6ccb650924393529a88/flight_path.csv";
    //$url = "http://predict.habhub.org/preds/a631a55508b7d9b65bd828f66f7c33c2c2fb2c17/flight_path.csv";
    $csv = array_map('str_getcsv', file($url));
    foreach ($csv as  $value) {
        
        $fake_altitude += 400;
        $fake_temperature -= 0.7;
        $fake_humidity -= 0.2;
        
        
        $predictData = Array ("event_id" => "1",
                      "latitude" => $value[1],
                      "longitude" => $value[2],
                      "altitude" => $value[3]
        );
        $id = $db->insert ('prediction', $predictData);



        // Generate fake car data, based on predicted data
        $fake_carData = Array ("event_2_id" => "1",
                      "timestamp" => date("Y-m-d H:i:s", $value[0]),
                      "latitude" => $value[1] + (rand(0, 1) / 50),
                      "longitude" => $value[2] + (rand(0, 1) / 50)
        );
        //print_r($fake_carData);
        //echo "<br>";
        $id = $db->insert ('car', $fake_carData);


        $latitude_offset = rand(0, 1) / 100;
        $longitude_offset = rand(0, 1) / 100;

        // Generate fake balloon data, based on predicted data
        $fake_balloonData = Array ("event_id" => "1",
                      "timestamp" => date("Y-m-d H:i:s", $value[0]),
                      "latitude" => $value[1] + $latitude_offset,
                      "longitude" => $value[2] + $longitude_offset,
                      "temperature" => $fake_temperature,
                      "altitude" => $fake_altitude,
                      "humidity" => $fake_humidity,
                      "has_image" => $count % 4 == 0
                      //"image" => $fake_blob_image
        );
        
        print_r($fake_balloonData);
        echo "<br>";
        $id = $db->insert ('balloon', $fake_balloonData);

        $count++;

    }
    
    echo "Finished generation script";
?>