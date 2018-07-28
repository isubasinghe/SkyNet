// calculate route

var hub = [-37.795504, 144.964618];
var userDestination = [
[-37.810219, 144.962840],
[-37.811047, 144.972963],
[-37.817648, 144.967128]
];

        console.log(userDestination);



    function calculateAndDisplayRoute(directionsService, directionsDisplay, userDestination, hub) {
        var waypts = [];
        var checkboxArray = userDestination;


        console.log(userDestination);

        var locationToPush = null;
        var hubCoords = null;
        for (var i = 0; i < checkboxArray.length; i++) {
          if (checkboxArray[i] != null) {

            locationToPush = {lat: checkboxArray[i][0], lng: checkboxArray[i][1]};

            waypts.push({
                location: locationToPush,
                stopover: true
              });

          }
        }

        hubCoords = {lat: hub[0], lng: hub[1]};

        directionsService.route({
          origin: hubCoords,
          destination: hubCoords,
          waypoints: waypts,
          optimizeWaypoints: true,
          travelMode: 'DRIVING'
        }, function(response, status) {
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