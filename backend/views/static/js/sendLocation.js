// Send Location to Server


window.onload = function() {
	document.getElementById('submit-id').onsubmit()=function() {
		alert('hi');
	}
}

function sendLocation() {
	var xhr = new XMLHttpRequest();
var url = "vpool.tech";
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
    }
};


coordsJSON = JSON.stringify(coords);
xhr.send(coordsJSON);
console.log('this funnction runs YAY');
}