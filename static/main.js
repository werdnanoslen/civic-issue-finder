// Resize iframe to fit content
function resize() {
  var newheight = document.getElementById("widget").contentWindow.document.body.scrollHeight;
  document.getElementById("widget").height = newheight + "px";
}

function search() {
    var url = "/geeks/civicissues/widget?labels=help wanted&number=12&body=";
    var query = document.getElementById('project-search-bar').value;
    document.getElementById('widget').src = url + query;
}
