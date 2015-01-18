{extends file="frontend/base.tpl"}
{block name="head_extra"}
<script>
function initialize() {
  var myLatlng = new google.maps.LatLng(52.2350939,5.9692556);
  var mapOptions = {
    zoom: 10,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('balloon-map'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Hello World!'
  });
    var i = 52.2350939;
   function updatePosition() {
        //myLatlng
        //window.alert(5 + 6);
        
        myLatlng = new google.maps.LatLng(i + 0.2350939,5.9692556);
        
          var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Hello World!'
  });

    };

    $(function() {
        setInterval("updatePosition()", 1000) // 300,000 miliseconds is 5 minutes       
        
        
    });
    
    
      var flightPlanCoordinates = [
    new google.maps.LatLng(52.2350939,5.9692556),
    new google.maps.LatLng(52.3350939,5.3692556),
    new google.maps.LatLng(52.6350939,5.6692556),
    new google.maps.LatLng(52.4350939,5.7692556)
  ];
  var flightPath = new google.maps.Polyline({
    path: flightPlanCoordinates,
    geodesic: true,
    strokeColor: '#0000FF',
    strokeOpacity: 0.8,
    strokeWeight: 3
  });

  flightPath.setMap(map);
}


google.maps.event.addDomListener(window, 'load', initialize);
 </script>
{/block}
{block name="container"}
      <div id="balloon-map">1</div>      
{/block}
