// Send Location to Server

function sendLocation() {
	var xhr = new XMLHttpRequest();
var url = "vpool.tech";
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(json);
    }
};


coordsJSON = JSON.stringify(coords);
xhr.send(coordsJSON);
console.log('this funnction runs YAY');
}