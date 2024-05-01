var url = window.location.pathname; // Get url of current webpage
var filename = url.substring(url.lastIndexOf('/')+1,url.lastIndexOf('.')) // Get filename of current webpage

if (filename.includes("/")){ // this page was found through a url with a directory only (/misalmon/dev/) instead of with page filename (/misalmon/dev/index.html)
  filename = document.getElementById("pageName").innerHTML
}

// config
var SETTINGS_URL_GENERAL = "../config/general.txt"
// page stuff
var SCRIPTS_URL = "../config/pageScripts.txt"
var NAV_URL = "../content/navigation.txt"
var TEMPLATE_HEADER_URL = '../template/header.txt'
var TEMPLATE_CONTENT_URL = '../template/content.txt'
var TEMPLATE_FOOTER_URL = '../template/footer.txt'
var CONTENT_URL = '../content/' + filename + ".txt"; // Get the content for this webpage

var navLinksText;
var scriptsText; // stores scripts to be called
var tempHeader; // stores template for header section
var tempFooter; // stores template for footer section
var tempContent; // stores template for content section
var storedText; // to store the page's contents as text

var config_general; // stores config info to be converted to json

//console.log("FILENAME JS: "+filename)

function setInnerHtml(elm, html) { // allows scripts tags to be set to inner html, but also be able to run at the same time
  elm.innerHTML = html;
  Array.from(elm.querySelectorAll("script")).forEach(oldScript => {
    const newScript = document.createElement("script");
    Array.from(oldScript.attributes)
      .forEach(attr => newScript.setAttribute(attr.name, attr.value));
    newScript.appendChild(document.createTextNode(oldScript.innerHTML));
    oldScript.parentNode.replaceChild(newScript, oldScript);
  });
}

/* BEGIN fetch content */
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
/* END fetch content */

/* BEGIN fetch navigation */
fetch(NAV_URL)
.then(function(response) {
  response.text().then(function(fetchedNav) {
    console.log("NAV: "+fetchedNav)
    navLinksText = fetchedNav;
  });
});
/* END fetch navigation */

/* BEGIN fetch settings */
fetch(SETTINGS_URL_GENERAL)
.then(function(response) {
  response.text().then(function(fetchedSettings_general) {
    console.log("SETTINGS_general: "+fetchedSettings_general)
    config_general = fetchedSettings_general;
  });
});
/* END fetch settings */

/* BEGIN ensures dynamicPage.js runs after page content has loaded */
let scriptsDiv = document.getElementById("scripts")
let pageContentBox = document.getElementById('writePageBox') // get box where we write page content

// allows us to monitor changes in innerhtml
var MutationObserver = window.MutationObserver || window.WebKitMutationObserver || window.MozMutationObserver;
var observer = new MutationObserver(onPageContentWritten);
observer.observe(pageContentBox, {
  childList: true
});

function onPageContentWritten(e){ // when the page content has been written
  console.log("Page Contents Changed")
  setInnerHtml(scriptsDiv,scriptsText) // run this script
}

fetch(SCRIPTS_URL)
.then(function(response) {
  response.text().then(function(fetchedScripts) {
    //console.log("SCRIPTS: "+fetchedScripts)
    scriptsText = fetchedScripts
  });
});
/* END after-page load dynamicPage.js */

//console.log("JAVASCRIPT_HEADER2:"+tempHeader)
