// sends clicked element's id
function trackClick(event) {
    var elementId = event.target.id;  // Get the ID of the clicked element
    // Send an AJAX request to the Flask server with the clicked element's ID
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/track_click', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ 'element_id': elementId }));
}

// Attach the click event listener to the desired elements on the page
var elements = document.getElementsByClassName('trackable');
for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', trackClick);
}