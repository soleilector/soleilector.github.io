var url = window.location.pathname; // Get url of current webpage
var filename = url.substring(url.lastIndexOf('/')+1,url.lastIndexOf('.')) // Get filename of current webpage

if (filename.includes("/")){ // this page was found through a url with a directory only (/misalmon/dev/) instead of with page filename (/misalmon/dev/index.html)
filename = document.getElementById("pageName").innerHTML
}

var TEMPLATE_HEADER_URL = 'template/header.txt'
var TEMPLATE_CONTENT_URL = 'template/content.txt'
var TEMPLATE_FOOTER_URL = 'template/footer.txt'
var CONTENT_URL = 'content/' + filename + ".txt"; // Get the content for this webpage

var tempHeader; // stores template for header section
var tempFooter; // stores template for footer section
var tempContent; // stores template for content section
var storedText; // to store the page's contents as text

//console.log("FILENAME JS: "+filename)

fetch(CONTENT_URL)
.then(function(response) {
  response.text().then(function(text) {
    storedText = text;
  });
});

fetch(TEMPLATE_HEADER_URL)
.then(function(response) {
  console.log("RESPONSE:"+response)
  console.log("RESPONSE TEXT: "+response.text)
  response.text().then(function(headerText) {
    tempHeader = headerText;
  });
});

fetch(TEMPLATE_CONTENT_URL)
.then(function(response) {
  response.text().then(function(contentText) {
    tempContent = contentText;
  });
});

fetch(TEMPLATE_FOOTER_URL)
.then(function(response) {
  response.text().then(function(footerText) {
    tempFooter = footerText;
  });
});

//console.log("JAVASCRIPT_HEADER2:"+tempHeader)
