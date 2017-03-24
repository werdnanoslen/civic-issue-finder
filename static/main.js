// Resize iframe to fit content
function resize() {
  var newheight = document.getElementById("widget").contentWindow.document.body.scrollHeight;
  document.getElementById("widget").height = newheight + "px";
}

function search() {
    var url = "/geeks/civicissues/widget?number=12&body=";
    var query = document.getElementById('project-search-bar').value;
    var labels = document.getElementById('project-label-search');
    var label = labels.options[labels.selectedIndex].text;
    document.getElementById('widget').src = url + query + "&labels=" + label;
    document.getElementById('currentLabel').innerHTML = label;
}
