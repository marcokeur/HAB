var updateTimes = 0;
  
var enableReFocus = true;
var altitude = 12340;
var burstAltitude = 35000;
var temperature = -14;
var humidity = 42;

var predictedLandingSite = new google.maps.LatLng(53.2350939,6.9692556);
var launchSite = new google.maps.LatLng(52.2350939,5.9692556);
var mapOptions = {
    zoom: 10,
    center: launchSite
}

var map = new google.maps.Map(document.getElementById('balloon-map'), mapOptions);

var marker = new google.maps.Marker({
      position: launchSite,
      map: map,
      title: 'Hello World!'
});
var landingMarker = new google.maps.Marker({
      position: predictedLandingSite,
      map: map,
      title: 'Predicted Landing Site!'
});

google.maps.event.addDomListener(window, 'load');


/*
* Some JSON from the server as replay.
*/

var serverResponse = '{ "name": "John", "latitude": "52.2350939", "longitude": "5.9692556" }' ; 
var obj = jQuery.parseJSON( serverResponse );

//$("#balloonLatitude").html(obj.latitude);
//$("#balloonLongitude").html(obj.longitude);

var latitude = 52.2350939;
var longitude = 5.9692556;

var carlatitude = 52.2350939;
var carlongitude = 5.9692556;

var carCoordinates = [];
var flightPlanCoordinates = [];
var flightPath = new google.maps.Polyline({
    path: flightPlanCoordinates,
    geodesic: true,
    strokeColor: '#0000FF',
    strokeOpacity: 0.8,
    strokeWeight: 3
});
var carPath = new google.maps.Polyline({
    path: carCoordinates,
    geodesic: true,
    strokeColor: '#000000',
    strokeOpacity: 0.8,
    strokeWeight: 3
});

flightPath.setMap(map);
carPath.setMap(map);

function updatePosition() {
    updateTimes++;
    
    latitude += (Math.random() / 100);
    longitude += (Math.random() / 80);
    var newPos = new google.maps.LatLng(latitude,longitude);

    carlatitude += (Math.random() / 100);
    carlongitude += (Math.random() / 80);
    var newCarPos = new google.maps.LatLng(carlatitude,carlongitude);

    
    flightPath.getPath().push(newPos);
    carPath.getPath().push(newCarPos);
    
    if (enableReFocus) {
        map.setCenter(newPos);
    }
    
    var distance = calculateDistance(launchSite.lat(), launchSite.lng() , newPos.lat(), newPos.lng());
    distance = Math.round(distance * 100) / 100
 
    altitude += 18;
    temperature -= Math.random();
    
    $("#balloonLatitude").html(Math.round(latitude * 10000) / 10000);    
    $("#balloonLongitude").html(Math.round(longitude * 10000) / 10000);     
    $("#distanceFromSite").html(distance);    
    $("#altitude").html(altitude);    
    //$("#altitudeProgressbar").html(altitude);  
    
    
    var altitudePercentage = (altitude /  burstAltitude) * 100;
    
    $('#altitudeProgressbar').css('width', altitudePercentage+'%').attr('aria-valuenow', altitudePercentage);        
    $('#temperature').html(Math.round(temperature * 100) / 100);
    $('#humidity').html(Math.round(humidity * 100) / 100);
    
    landingDifference = calculateDistance(predictedLandingSite.lat(), predictedLandingSite.lng() , newPos.lat(), newPos.lng());
    $("#landingDifference").html(Math.round(landingDifference * 100) / 100);    
    
    
    if (updateTimes % 60 == 0) {    
        marker = new google.maps.Marker({
          position: newPos,
          map: map,
          title: 'Hello World!'
        });  
    }
    
    if (updateTimes == 200) {
        clearInterval(refreshIntervalId);
    }
     
};

//landingMarker


$("#enabletracking").click(function() {
    enableReFocus = !enableReFocus;
    
    if (enableReFocus) {
        $("#enabletracking").html("Disable Auto Tracker");
    }else{
        $("#enabletracking").html("Enable Auto Tracker");
    }
    
    
});

var refreshIntervalId;
$(function() {
    refreshIntervalId = setInterval("updatePosition()", 1000)
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
