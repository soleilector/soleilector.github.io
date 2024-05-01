console.log("LOADED AND RUNNING[dynamicPage.js]...")
/* BEGIN chart */
let charts = {} // charts catalog
let foundCharts;

function separateValues(chartId){
    chartObj = charts[chartId]
    list = chartObj["values"]
    defaultColor = chartObj["defaultColor"]
    
    x_values = []
    y_values = []
    colors = []
    
    for (itemId=0;itemId<list.length;itemId++) {
        thisItem = list[itemId] // get the obj holding this data value item
        x_values[x_values.length] = thisItem[0]
        y_values[y_values.length] = thisItem[1]
        
        console.log("CL:"+colors.length+"==XL"+x_values.length)
        
        // set this color to its given color or the defined color, if absent
        if (thisItem[2] == "") {
            console.log("USED default color i#"+itemId)
            colors[colors.length] = chartObj["defaultColor"]
        } else {
            console.log("USED defined color i#"+itemId)
            colors[colors.length] = thisItem[2]
        }
    }
    
    returnData = {
        "x" : x_values,
        "y" : y_values,
        "colors" : colors
    }
    
    console.log("RETURNED DATA: "+returnData)
    
    return returnData
}

function initCharts(){ // initialize charts into catalog
    foundCharts = document.getElementsByClassName('chart')
    
    for (chartId=0; chartId < foundCharts.length; chartId++) { // for each chart found
        thisChartObj = foundCharts[chartId]
        
        canvas = thisChartObj.getElementsByClassName("chartCanvas")[0] // get first child of class <chartCanvas>
        chartTypeObj = thisChartObj.getElementsByClassName('chartType')[0]
        
        chart_yValueRangesObj = thisChartObj.getElementsByClassName('chartYRange')[0]
        yrange_min = parseInt(chart_yValueRangesObj.min)
        yrange_max = parseInt(chart_yValueRangesObj.max)
        
        chartValues = []
        chartValueElems = thisChartObj.getElementsByClassName("chartValue")
        chartDefaultClrObj = thisChartObj.getElementsByClassName("chartDefaultClr")[0]
        
        console.log("Y-VAL range: "+chart_yValueRangesObj.min+"<=>"+chart_yValueRangesObj.max)
        
        if (chartValueElems.length > 0) { // if there is more than one chart element
            // catalog the chart's values
            for (valId=0;valId<chartValueElems.length;valId++){ // for each value element found
                valIdObj = chartValueElems[valId]
                valIdObj_value = valIdObj.value
                
                xy_values = valIdObj_value.split(",") // split xy values by ',' delimiter
               
                chartValues[chartValues.length] = [
                    parseInt(xy_values[0]),
                    parseInt(xy_values[1]),
                    valIdObj.style.color
                    ]
            }
        }
        
        chartInfo = { // info for this chart
            "obj" : thisChartObj,
            "values" : chartValues, // values associated with this chart
            "defaultColor" : chartDefaultClrObj.value || "blue"
        }
        
        console.log("VALUE INFO: \n\t"+chartInfo["values"]+"\n\t"+chartInfo["defaultColor"])
        
        charts[chartId] = chartInfo // add chart info to charts box
        
        console.log("CHART ID: "+chartId)
        
        drawChart(chartId)
    }
}

function reloadCharts() { // updates charts catalog with new entries and updates older/removed entries
    
}

function drawChart(chartId){ // visually draws the chart
    thisChartInfo = charts[chartId]
    console.log(Object.keys(charts).length)
    console.log(charts)
    console.log(thisChartInfo)
    
    if (thisChartInfo != null && thisChartInfo != undefined) { // if this chart info exists
        console.log("exists")
        chartObj = thisChartInfo["obj"] // chart dom object
        chartValues = thisChartInfo["values"]
        
        console.log("VALUES: "+chartValues)
            
        sep_XYValues = separateValues(chartId)
        
        console.log("SEPVALUES_X: "+sep_XYValues["x"])
        console.log("SEPVALUES_Y: "+sep_XYValues["y"])
        console.log("SEPVALUES_CLR: "+sep_XYValues["colors"])
        console.log("CHART_TYPE: "+chartTypeObj.value)
        
        new Chart(canvas.id,{
            "type" : chartTypeObj.value,
            "data" : {
                "labels" : sep_XYValues["x"],
                "datasets" : [{
                    fill: false,
                    lineTension: 0,
                    backgroundColor : sep_XYValues["colors"],
                    borderColor : "rgba(0,0,255,0.1)",
                    data : sep_XYValues["y"]
                }]
            },
            "options" : {
                legend : {display:false},
                scales: {
                  yAxes: [{ticks: {
                                        min: yrange_min,
                                        max: yrange_max
                                    }}],
                }
            }
        })
        
        console.log("CANVAS ID: "+canvas.id)
    }
}
/* END chart */

/* BEGIN tabbed Boxes */
//** catalogs and navigates tabbed boxes on webpage
let tabBoxes = {}
let foundTabbedBoxes;

function myClickHandler(e) { // if we happen to click on a tab...
    let name = e.target.name;
    if (name != undefined && name != null) {
        let hashPos = name.search("#tab#") // check if we clicked on something with a name that includes #tab#
        if (hashPos != -1) {
            //alert(name);
            showTab_External(name)
        }
    }
}

function showTab_External(tabId) { // if navigation done externally, such as clicking a timeline above it...
    //console.log("Showing tab: "+tabId)
    tabInfoObject = document.getElementById(tabId); // found the tab Info
    
    //console.log("INNER HTML: "+tabInfoObject.innerHTML)
    
    tabBoxKeys = Object.keys(tabBoxes) // keys for each tabbed box
    //console.log("KEY COUNT: "+tabBoxKeys.length)
    //console.log("KEYS for each tabbed box: "+tabBoxKeys)
    
    for (keyId = 0; keyId < tabBoxKeys.length; keyId++){ // for each key
        this_tabBox = tabBoxes[keyId] // get info for this tabbed Box
        
        //console.log("TABBOX_KEYID["+keyId+"]: "+this_tabBox)
        
        tabBoxInfo_tabInfos = this_tabBox["tabInfo"] // get tab infos for this tabbed Box
        
        tabInfo_Ids = Object.keys(tabBoxInfo_tabInfos) // get Ids of this tabbed box's tabbed infos
        
        //console.log("NUM_TABINFO_KEYS: "+tabInfo_Ids)
        
        for (infoIdCt = 0; infoIdCt < tabInfo_Ids.length; infoIdCt++) { // for each id of tabbed box's tabbed infos
            infoId = tabInfo_Ids[infoIdCt] // get the id using the infoIdCt as an index to the tabInfo_Ids array
            this_tabInfoObject = tabBoxInfo_tabInfos[infoId] // get this particular info box of the tabbed box
            
            //console.log("TABBOXINFO_ID: "+infoId)
            
            if (infoId == tabId && this_tabInfoObject == tabInfoObject) {
                this_tabInfoObject.style.display = "block"
            } else {
                this_tabInfoObject.style.display = "none"
            }
        }
    }
}

function initTabbedBoxes(){
    foundTabbedBoxes = document.getElementsByClassName("tabInfoContainer")
    
    //** catalog all found tabbed boxes with relevant info
    for (boxId=0; boxId < foundTabbedBoxes.length; boxId++) {
        let thisTabbedBox = foundTabbedBoxes[boxId] // get tabbed box object
        
        let thisBoxTabs = thisTabbedBox.getElementsByClassName("tab") // get tabs for tabbed box object
        let thisBoxTabInfo = thisTabbedBox.getElementsByClassName("tabInfo") // get tab info for tabbed box object
        
        // catalog all tab info boxes by their id's
        catalogued_tabBoxes = {}
        for (infoId = 0; infoId < thisBoxTabInfo.length; infoId++) {
            this_tabInfo = thisBoxTabInfo[infoId]
            tabId = this_tabInfo.id
            
            catalogued_tabBoxes[tabId] = this_tabInfo
            
            if (infoId == 0) {
                this_tabInfo.style.display = "block"
            } else {
                this_tabInfo.style.display = "none"
            }
        }
        
        // define dictionary for this tab Box
        tabBoxInfo = {
            "currentTab" : Object.keys(catalogued_tabBoxes)[0], // specify current tab to be first cataloged tab Id
            "box" : thisTabbedBox, // get this tabbed box
            "tabs" : thisBoxTabs, // get the navigation tabs for this tab box, if possible
            "tabInfo" : catalogued_tabBoxes //
        }
        
        tabBoxes[boxId] = tabBoxInfo
        //COMMENT console.log("CATALOGUED BOXES: "+tabBoxes[boxId]["tabInfo"])
    }
    
    //** show tab based on url
    pageLink = window.location.href
    //console.log("HREF: "+pageLink)
    hashPos = pageLink.search("#") // are we navigating to a part of the webpage
    if (hashPos > -1) { // we found the hashtag
        console.log("HASH HREF EXISTS")
        
        tabInfo_name = pageLink.substring(hashPos) // grab the name of the tabInfo
        tabInfo_Id = "#tab" + tabInfo_name
        
        console.log(tabInfo_Id)
        
        tabInfoObject = document.getElementById(tabInfo_Id) // we got the element
        if (tabInfoObject != null && tabInfoObject != undefined) { // only if we have a corresponding tab element do we show the tab
            showTab_External(tabInfo_Id)
        }
    }
    
    //** set click handler for clicking tabs of a tabbed box 
    document.onclick = myClickHandler;
}

/* END tabbed boxes */

/* BEGIN auto slideshow detection and configuration */
let slideObjects = {}
let slideShows;

// get number of slideshow objects in document
function getNumSlideObjects(){                    
    return Object.keys(slideObjects).length
}

function setCurrentSID(ssId,sId){
    let slideShowObject = slideObjects[ssId] // get slideshow object
    slideShowObject["currentSID"] = sId
}

// get the slide previous to given slide id
function getPrevSlideId(ssId,slideId) { 
    let slideShowObject = slideObjects[ssId] // get slideshow object
    let slideShow_slides = slideShowObject["slides"] // get the slides for this slideshow object
    
    //console.log("current slide Id(getprevslide): "+slideId)
    
    let prevSlideId = slideId - 1 // subtract one from slide id
    
    //console.log("unadjusted prevslideId: "+prevSlideId)
    
    if (prevSlideId < 0) { // correct if less than 0
        prevSlideId = slideShow_slides.length - 1 // set to maximum slide id
    }
    
    //console.log("adjusted prevslideId: "+prevSlideId)
    
    return prevSlideId // return previous slide id
}

// sets current slide id to the id of the previous slide
function jumpPrevSlide(ssId){ 
    let slideShowObject = slideObjects[ssId] // get slideshow object
    let slideShow_sId = slideShowObject["currentSID"] // get current slide id for slideshow object
    
    let currentSlideId = slideShow_sId - 1 // subtract one from current slide id
    
    if (currentSlideId < 0){ // if slide Id is less than 0
        currentSlideId = slides.length - 1 // correct to maximum slide id
    }
    
    setCurrentSID(ssId,currentSlideId)
}

// proceed to next slide
function jumpNextSlide(ssId) { 
    let slideShowObject = slideObjects[ssId] // get slideshow object
    let slideShow_slides = slideShowObject["slides"] // get the slides for this slideshow object
    let slideShow_sId = slideShowObject["currentSID"] // get current slide id for slideshow object
    
    let currentSlideId = slideShow_sId + 1 // subtract one from current sId
    
    if (currentSlideId >= slideShow_slides.length) { // if slide id is more than maximum
        currentSlideId = 0 // set to initial slide id
    }
    
    setCurrentSID(ssId,currentSlideId)
}

// reload slides for page; adjusts visuals to match data
function reloadSlides(ssId) { 
    let slideShowObject = slideObjects[ssId] // get slideshow object
    //console.log(Object.keys(slideObjects))
    
    let slideshow_container = slideShowObject["container"]
    let slideShow_sId = slideShowObject["currentSID"] // get slideshow object's current slideId
    let slideShow_slides = slideShowObject["slides"] // get slideshow object's slides
    
    //console.log("passing current sId: "+slideShow_sId)
    
    prevSlideId = getPrevSlideId(ssId, slideShow_sId) // get previous slide id
    //console.log(prevSlideId)
    prevSlide = slideShow_slides[prevSlideId] // get the previous slide
    
    //console.log("Current Slide Id: "+slideShow_sId)
    //console.log("Previous slide Id: "+prevSlideId)
    
    /* BEGIN EASE; (UNNECESSARY 4 FUNCTION; nice 2 have) */
        // sets background to previous image so current image will fade onto the background
        // otherwise, each image fades from white into full opacity
    imgSrc = prevSlide.children[0].getAttribute('src'); // find the slide's image
    //console.log("IMAGE SRC "+imgSrc)                   // testing 
    slideshow_container.style.backgroundImage = "url('" + imgSrc + "')" // set the background of the slide's container
    /* END EASE */
    
    for (thisSlideId = 0; thisSlideId < slideShow_slides.length; thisSlideId++) {
        thisSlide = slideShow_slides[thisSlideId] // get slide associated with this slideId
        
        if (thisSlideId == slideShow_sId) { // if thisSlideId is equivalent to current slide's Id
            thisSlide.style.display = "block" // make it visible
        } else { // this slide is not current slide
            thisSlide.style.display = "none" // make it invisible
        }
    }
}

function autoSlide(ssId){
    jumpNextSlide(ssId)
    reloadSlides(ssId)
    //console.log("slides changed")
    setTimeout(function(){
            autoSlide(ssId)
        },5000)
}

function initSlideShows(){
    // get all slideshows defined within webpage
    slideShows = document.getElementsByClassName("slideshowContainer")

    // catalog all slideshows in webpage with relevant information
    for (ssId = 0; ssId < slideShows.length; ssId++) { // for each slideshow container found...
        let slideShowObject = slideShows[ssId]
        
        slideShowInfo = {
            "container" : slideShowObject,
            "slides" : slideShowObject.getElementsByClassName("slideshow"),
            "currentSID" : 0,
            "enabled" : true
        }
        
        slideObjects[getNumSlideObjects()] = slideShowInfo
        console.log(slideObjects[0]["currentSID"])
        console.log(getNumSlideObjects())

    }

    // activate slides
    for (ssId = 0; ssId < getNumSlideObjects(); ssId++) {
        this_slideShowObject = slideObjects[ssId]
        
        reloadSlides(ssId)
        autoSlide(ssId)
    }
}
/* END slideShows */

/* initialize everything */
initCharts()
initTabbedBoxes()
initSlideShows()
