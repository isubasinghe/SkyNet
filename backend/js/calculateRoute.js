// calculate route

// var hub = [-37.795504, 144.964618];
// var userDestination = [
// [-37.810219, 144.962840],
// [-37.811047, 144.972963],
// [-37.817648, 144.967128]
// ];

// console.log(userDestination);



function calculateAndDisplayRoute(userDestination, hub) {
  var waypts = [];

  console.log(userDestination);

  var locationToPush = [];
  var hubCoords = new google.maps.LatLng(hub[0], hub[1]);

  userDestination.forEach(element => {
    locationToPush.push({ "location": new google.maps.LatLng(element[0],element[1]),"stopover":true});
  });

  hubCoords = hub[0]+","+hub[1];

  directionsService.route({
    origin: hubCoords,
    destination: hubCoords,
    waypoints: locationToPush,
    optimizeWaypoints: true,
    travelMode: 'DRIVING'
  }, function (response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
      var route = response.routes[0];
      var summaryPanel = document.getElementById('directions-panel');
      summaryPanel.innerHTML = '';
      // For each route, display summary information.
      for (var i = 0; i < route.legs.length; i++) {
        var routeSegment = i + 1;
        summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment +
          '</b><br>';
        summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
        summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
        summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
      }
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}