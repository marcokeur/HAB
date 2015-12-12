var app = angular.module('habApp', ['uiGmapgoogle-maps']);

app.controller('sensorCtrl', function($scope, $http, $timeout, uiGmapGoogleMapApi) {

    // Google Maps
    $scope.map = { center: { latitude: 52.2211, longitude: 5.9766 }, zoom: 11 };
    $scope.polylines = [];

    $scope.balloonDataCurrentIndex = 0;
    $scope.lastUpdateBalloonId = 0;
    $scope.lastUpdateCarId = 0;
    
    $scope.liveActive = true;
    
    $scope.carPathVisible = false;
    
    $http.get("https://hab-henryfinlandia.c9users.io/backend/measurement.php").then(function(response) { 
        
        // Fetch next balloon data measurement
        $scope.nextSlide = function () {
            $scope.balloonDataCurrentIndex = ($scope.balloonDataCurrentIndex < $scope.balloonList.length - 1) ? ++$scope.balloonDataCurrentIndex :  $scope.balloonList.length - 1; //0;
            $scope.balloonData = $scope.balloonList[$scope.balloonDataCurrentIndex];
            $scope.carData = $scope.carList[$scope.balloonDataCurrentIndex]; // Note for fix later, cant use balloonIndex 
            
            //$scope.landingDifference = calculateDistance($scope.landingLocation.latitude, $scope.landingLocation.longitude, $scope.balloonData.latitude, $scope.balloonData.longitude);
            
            
            if ($scope.balloonData != null) {
                // Update balloon image.
                if ($scope.balloonData.has_image) {
                        $scope.balloonImage = "img/photos/" + $scope.balloonData.id + ".jpg";
                }
                
                  $http.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + $scope.balloonData.latitude +"," + $scope.balloonData.longitude).then(function(response) { 
       
                        if (response.data.status == "OK") {
       
                            //console.log(response.data);
    
                            $scope.balloonDataArea = response.data.results[0].formatted_address;
                        }
                 });
             
            }
        };

        // Fetch previous balloon data measurement
        $scope.prevSlide = function () {
            $scope.balloonDataCurrentIndex = ($scope.balloonDataCurrentIndex > 0) ? --$scope.balloonDataCurrentIndex : 0; // $scope.balloonList.length - 1;
            $scope.balloonData = $scope.balloonList[$scope.balloonDataCurrentIndex];
            $scope.carData = $scope.carList[$scope.balloonDataCurrentIndex]; // Note for fix later, cant use balloonIndex 
            
            //$scope.landingDifference = calculateDistance($scope.landingLocation.latitude, $scope.landingLocation.longitude, $scope.balloonData.latitude, $scope.balloonData.longitude);
            
            if ($scope.balloonData != null) {
                  if ($scope.balloonData.has_image) {
                        $scope.balloonImage = "img/photos/" + $scope.balloonData.id + ".jpg";
                  }
    
                    $http.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + $scope.balloonData.latitude +"," + $scope.balloonData.longitude).then(function(response) { 
       
                        if (response.data.status == "OK") {
       
                            //console.log(response.data);
    
                            $scope.balloonDataArea = response.data.results[0].formatted_address;
                        
                        }
                 });
            }

        };
        
        
        $scope.togglePath = function(array) {
            $scope.polylines[array].visible = !$scope.polylines[array].visible;
        };
        
         $scope.goLive = function(array) {
            console.log("Live!, track and trace latest balloon/car data");
            $scope.liveActive = true;
        };
        
         $scope.goReplay = function(array) {
            console.log("Replay, Use the slider to see the balloon measurements");
            $scope.liveActive = false;
        };
        
        //console.log(response.data);
        if (response.data.length != 0) {
            
           
            
            // Store data in seperate variables
            $scope.balloonList = response.data.balloon;
            $scope.carList = response.data.car;
            $scope.predictionList = response.data.prediction;
            
            
            // Landing location is know, last predicted element.
            $scope.landingLocation = $scope.predictionList[$scope.predictionList.length -1];
            
            // Update balloonData current view
            
            if ($scope.balloonList.length > 0) {
                
                 $scope.map = { center: { latitude: $scope.balloonList[$scope.balloonList.length -1].latitude, longitude: $scope.balloonList[$scope.balloonList.length -1].longitude }, zoom: 11 };

                
                $scope.balloonData = $scope.balloonList[$scope.balloonDataCurrentIndex];
                $scope.lastUpdateBalloonId = $scope.balloonList[$scope.balloonList.length -1].id;
            }
        }
        
    }).then(function() {

        // Update google maps with the balloon measurement data, car data and predicted balloon path. 
          uiGmapGoogleMapApi.then(function(){
              $scope.polylines = [
                {
                    id: 1,
                    path: $scope.balloonList,
                    stroke: {
                        color: 'red',
                        weight: 3
                    },
                    geodesic: true,
                    visible: true,
                },
                {
                    id: 2,
                    path: $scope.carList,
                    stroke: {
                        color: 'blue',
                        weight: 3
                    },
                    geodesic: true,
                    visible: true
                },
                {
                    id: 3,
                    path: $scope.predictionList,
                    stroke: {
                        color: 'green',
                        weight: 3
                    },
                    geodesic: true,
                    visible: true
            }
        
            ];
            });

        });

    
   
   
    // Fetch the latest data and push/store them in the controller.
    $scope.getData = function(){
        
        
        // Check wether we are live to perform 30s polling.
        //if (event_data == active)
  

    var realtimeUrl = "https://hab-henryfinlandia.c9users.io/backend/realtime.php?balloon_id=" + $scope.lastUpdateBalloonId + "&car_id=" + $scope.lastUpdateCarId;
    console.log(realtimeUrl);

    $http.get(realtimeUrl)
     .then(function(response) { 
        
        if (response.data.length != 0) {
            
            if (response.data.balloon.length > 0) {

                for (i = 0; i < response.data.balloon.length; i++) { 
                    $scope.lastBalloonData = response.data.balloon[i];
                    $scope.lastUpdateBalloonId = $scope.lastBalloonData.id; 
                }
                
                
                
                // if ($scope.lastBalloonData.has_image) {
                //     $scope.balloonImage = "img/photos/" + $scope.lastBalloonData.id + ".jpg";
                // }
                
                console.log("add balloon data: " + $scope.polylines[0].path.length);
                $scope.polylines[0].path.push($scope.lastBalloonData);
            }
            
            if (response.data.car.length > 0) {
                
                for (i = 0; i < response.data.car.length; i++) { 
                    $scope.lastCarData = response.data.car[i];
                    $scope.lastUpdateCarId = $scope.lastCarData.id; 
                }
                
               $scope.polylines[1].path.push($scope.lastCarData);  
               console.log("add car data: " + $scope.polylines[1].path.length);
                
              
                //console.log("car size: " +$scope.polylines[1].path.length);
             }
            
        
        }
        //console.log(response.data.balloon[0].longitude);
        
        //new google.maps.LatLng(-34, 151)
        
        //console.log($scope.polylines);
        
        if (response.data.length != 0) {

            //$scope.balloondata.push(response.data.balloon);
            //$scope.cardata.push(response.data.car);
        
            //$scope.tripdata.balloon.push(response.data.balloon);
            
            
            //$scope.polylines[0].path.push(response.data.balloon[0]);
        }        
    });
    };
  
  
   
//   // Run function every second
   setInterval($scope.getData, 10000);


    $scope.insertFakeData = function () { 
        $http.get("https://hab-henryfinlandia.c9users.io/website/backend/predictPath_fakedata.php") 
        .then(function(response) { 
            console.log(response.data);
        })
    };
    

    $scope.clearDatabase = function () { 
        $http.get("https://hab-henryfinlandia.c9users.io/backend/cleardatabase.php") 
        .then(function(response) { 
            console.log(response.data);
        })
    };

    
});


function calculateDistance(lat1, lon1, lat2, lon2) {
  var R = 6371; // km
  var dLat = (lat2 - lat1).toRad();
  var dLon = (lon2 - lon1).toRad();   
  var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(lat1.toRad()) * Math.cos(lat2.toRad()) * Math.sin(dLon / 2) * Math.sin(dLon / 2); 
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a)); 
  var d = R * c;
  return d;
}
Number.prototype.toRad = function() {
  return this * Math.PI / 180;
}
