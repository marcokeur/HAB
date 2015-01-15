{extends file="frontend/base.tpl"}
{block name=container}
      <div class="starter-template">        
        <button style="margin:10px;" type="button" class="pull-right btn btn-sm btn-info">Replay Event</button>
      </div>
      
       <div class="alert alert-info" role="alert">
        <strong>Launch Date!</strong> 28th of February.
      </div>
      
      
      <div class="row">
        <div class="col-md-8">
        <h2>Tracker</h2>            
        <div id="balloon-map">1</div>      
        
        
        <button id="enabletracking" style="margin:10px;" type="button" class="pull-left btn btn-sm btn-info">Disable Auto tracker</button>
        <button style="margin:10px;" type="button" class="pull-left btn btn-sm btn-info">Toggle recovery team</button>
        <button style="margin:10px;" type="button" class="pull-right btn btn-sm btn-info">Display balloon path</button>
        
        </div>
        <div class="col-md-4">
            <h2>Balloon Dashboard</h2>            
            <img width="100%" src="img/highaltitude.jpg"/>
            <p class="text-right">Last update: 1 minute ago <img src="http://www.morninginarizona.com/wp-content/plugins/tweet-blender/img/ajax-refresh-icon.gif"/></p>
            
            <h3>Location</h3>
            <p><b>Latitude</b>:<span id="balloonLatitude">-</span></p>
            <p><b>Longitude</b>:<span id="balloonLongitude">-</span></p>                      
            <hr/>                 
        </div>
      </div>
      
        <div class="row">
            <div class="col-md-6">
                <h3>Altitude</h3>
                <div class="progress">
                    <div id="altitudeProgressbar" class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width:80%">
                    <span class="sr-only">20% Complete</span>
                    <span class="pull-left">0km</span>
                    <span class="pull-right">altitude</span>
                    </div>                
                    <span class="pull-right">35000km</span>
                </div>  
                <p><span id="altitude">-</span> meter</p>                
                <hr/>
                <h3>Temperature</h3>
                <p><span id="temperature">-</span> degrees Celsius</p> 
                <hr/>
                <h3>Humidity</h3>
                <p><span id="humidity">-</span>%</p>
                <hr/>                
            </div>
            <div class="col-md-6">
                <div class="starter-template">        
                
                        
                
                <h3>Distance</h3>
                <p><span id="distanceFromSite">134</span> kilometer from launch site</p>                
                <hr/>
                <h4>Average Speed</h4>    
                <p>78 km/h</p>                
                <hr/>
                <h4>Predicted Landing Location</h4>                
                <p><b>Latitude</b>:52.2350939</p>
                <p><b>Longitude</b>:5.9692556</p>
                <p><span id="landingDifference"></span> kilometers from predicted landing site</p>                
                <hr/>
                </div>
            </div>
        </div>

       <div class="row">
            <div class="col-md-9">
                <h3>HAB Info</h3>
                <p>The most common type of high altitude balloons are weather balloons. Other purposes include use as a platform for experiments in the upper atmosphere. Modern balloons generally contain electronic equipment such as radio transmitters, cameras, or satellite navigation systems, such as GPS receivers.</p>
                
                <p>The most common type of high altitude balloons are weather balloons. Other purposes include use as a platform for experiments in the upper atmosphere. Modern balloons generally contain electronic equipment such as radio transmitters, cameras, or satellite navigation systems, such as GPS receivers.</p>
            </div>
            <div class="col-md-3">
                <h3>Pickup Team</h3>
                <p><b>Latitude</b>:52.2350939</p>
                <p><b>Longitude</b>:5.9692556</p>
            
                
            </div>
        </div>      
{/block}
