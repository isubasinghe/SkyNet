window.directionsService;
window.directionsDisplay;

initMap = function () {
    directionsService = new google.maps.DirectionsService;
    directionsDisplay = new google.maps.DirectionsRenderer;

    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: -37.809595,
            lng: 144.969874
        },
        zoom: 17
    });
    directionsDisplay.setMap(map);
}

function displayMessage(message) {
    document.getElementById("DesTitle").innerHTML = 'Your ride will arrive in ' + String(Math.round(message))+' mins';
}