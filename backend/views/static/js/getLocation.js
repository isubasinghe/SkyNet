var currentLocation = {    
	location: null, 
    circle: null, 
    marker: null
},
options = {
	enableHighAccuracy: true,
    timemout: Infinity,
    maximumAge: 0
}


var coords = {
    lat: null,
    lng: null,
    id: "user1"
}

if (navigator.geolocation){
	setTimeout(function() {holder = navigator.geolocation.watchPosition(showCurrentLocation, error, options);}, 1000);
}   
else {
	alert("GPS error: not available");
}


function error() {
	alert("Error: Geolocation not available.");
}


function showCurrentLocation(position)
{
    //variables for reference convinience
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;
    var accuracy = position.coords.accuracy;

    console.log('current accuracy: ' + accuracy)

    if (accuracy < 70) {
        coords.lat = latitude;
        coords.lng = longitude;
    }
    
    //create instance of LatLng class of google map everytime showCurrentLocation callback function is called
    currentLocation.location = new google.maps.LatLng(latitude, longitude);
    
    //set circle with radius is accuracy around current location of user
    if (currentLocation.circle === null)
        {
            currentLocation.circle = new google.maps.Circle({
            strokeColor: '#0080ff',
            strokeOpacity: 0.5,
            strokeWeight: 1,
            fillColor: '#3399ff',
            fillOpacity: 0.35,
            map: map,
            center: currentLocation.location,
            radius: accuracy,
          });
        }
    else
        {
            currentLocation.circle.setCenter(currentLocation.location);
            currentLocation.circle.setRadius(accuracy);
            
        }
    
    //set a marker at the current location of user    
    if (currentLocation.marker === null)
            {
                currentLocation.marker = new google.maps.Marker({
                    position: currentLocation.location, 
                    map: map,
                    icon: {
                        path: google.maps.SymbolPath.CIRCLE,
                        scale: 5,
                        fillColor: '#0080ff',
                        fillOpacity: 1,
                        strokeColor: 'white',
                        strokeWeight: 1.5
                    }
                });
                map.panTo(currentLocation.location);
            }
        else
    {
        currentLocation.marker.setPosition(currentLocation.location);
        map.panTo(currentLocation.location);
    }

}

