import os
import sys

import pyscript
beginLayout = ""
endLayout = ""
STYLING = """<style>
    /* NOTE TO SELF
        Setting width to 100%, then setting padding or margin of that object will extend it that size beyond 100%
            instead of setting padding inside to 50px!!!


    */
        /* STRUCTURAL CSS */
        *, html {
            margin:0;
            padding:0;

        }
        body {
            width:100%;
        }

        /* HEADER STUFF */
        header {
            width:100%;
            text-align:center;
            margin:0;
            padding:0;
        }
        header div.header { 
            margin:0px;
            padding:px;
            width:100%;
        }
        header div.header div.headerImg {
            width:100%;
            background:green;
        }
        header div.header div.headerImg img {
            background:gray;
            width:100%;
        }
        header div.header div.logo {
            background:darkslategray;
            padding-top:10px;
            padding-bottom:10px;
        }
        header div.header div.logo h1 {
            font-weight:bold;
            color:white;
        }

        /* NAVIGATION */
        div.header div.nav {
           width:100%;
        }

        div.header div.nav ul.nav {
            list-style-type:none; # prevents styling
            margin:0px;
            width:100%;
            display:inline-block; /* keeps from overflowing */
            background:black;
        }
        div.header div.nav ul.nav li {
            display:inline-block; /* Horizontally aligns list elemenets */
            font-weight:bold;
        }
        div.header div.nav ul.nav li a {
            display:block;
            color:black;
            text-align:center; 
            padding:10px;
            background:black;
            color:white;
            text-align:center;
        }
        div.header div.nav ul.nav li a:hover {
            background:cadetblue;
        }

        /* CONTENT */
        div.content {
            padding-top:10px;
            paddng-bottom:10px;
            width:100%;
        }
        div.content div.page_content {
            min-height:600px;
            width:100%;
            background:white;
        }
        div.content div.breadcrumbs {
            font-weight:bold;
            color:cadetblue;
            padding-left:20px;
        }

        /* COMMON ELEMENTS */
        div.content div.page_content h2 {
            width:80%;
            margin:auto;
            padding-top:20px;
            margin-bottom:20px;
            text-align:center;
            color:darkslategray;
            text-transform:lowercase;
            border-bottom:5px solid darkslategray;
        }
        div.content div.page_content h3 {
            padding-left:10px;
            padding-top:20px;
            padding-bottom:10px;
            text-transform:lowercase;
            color:darkslategray;
        }
        div.content div.page_content p {
            padding-left:20px;
            padding-bottom:10px;
            padding-top:10px;
            line-height:0.7;
        }

        /* BUTTONS */
        div.content div.page_content button {
            border-radius:5%;
            background:darkslategray;
            color:white;
            padding:20px;
            text-align:center;
            margin:10px;
            font-weight:bold;
            border:0px;
        }
        div.content div.page_content p button {
            padding:10px;
            margin: 5px;
        }
        div.content div.page_content button:hover {
            background:olive;
            color:white;
        }
        div.content div.page_content div.btnCntr {
            width:80%;
            margin:auto;

            /* BEGIN_A use this instead of display:block to center items in a row */
            display:flex;
            justify-content: center; /* center, space-around, space-between */
            /* END_A */
        }
        div.content div.page_content div.btnCntr button {

        }


        table.general {
            background:white;
            margin:20px;
        }
        table.general th {
            border-bottom:gray dotted 2px;
            min-width:300px;
            text-align:left;
            padding:10px;
            font-style:italic;
        }
        table.general td {
            padding:10px;
        }

        /* FOOTER STUFF */
        footer {
            width:100%;
            text-align:center;
            background:darkslategray;
            color:white;
            font-weight:bold;
            margin:0px;
        }
        footer p {
            padding:50px;
        }
    </style>"""
HEADER = """<header>
        <div class='header'> <!-- HEADER DIV -->
            <div class='logo'> <!-- LOGO -->
                <h1>{website_title}</h1> <!-- LOGO HEADER -->
            </div>
            <div class='nav'> <!-- BEGIN NAVIGATION HEADER -->
                <ul class='nav' id="navlinks"> <!-- NAVIGATION LINKS -->
                    {nav_links}
                </ul>
            </div> <!-- END NAVIGATION HEADER -->
            <div class='headerImg'> <!-- BEGIN HEADER IMG-->
                <img src='{header_image}'/> <!-- HEADER IMAGE -->
            </div> <!-- END HEADER IMG -->
        </div>
    </header>"""
NAV_LINKS = {
    "Home": "misalmon_home.html",
    "Lifecycle": "lifecycle.html",
    "Conservation": "conservation"
}
CONTENT = """
<div class="content"> <!-- BEGIN CONTENT -->
        <div class="breadcrumbs">
            <p>Index / Lifecycle</p>
        </div>
        <div class="page_content">
            <h2>{page_title}</h2>
            {page_content}
        </div>
    </div> 
"""
FOOTER = """
<footer> <!-- BEGIN FOOTER -->
        <p>{text}</p>
    </footer> <!-- END FOOTER -->
"""
WEBPAGE_EXTENSION = "html"
HEADER_IMAGE = "header.jpg"
WEBSITE_TITLE = "MichiganSalmon"


def formLink(page_name):
    extension = WEBPAGE_EXTENSION

    if WEBPAGE_EXTENSION != None and WEBPAGE_EXTENSION != "":
        extension = "." + WEBPAGE_EXTENSION

    return (page_name + extension)

def getStyling():
    return STYLING

def findPage(pgName):
    page_contents_list = os.listdir("./content/")

    for content_file_name in page_contents_list: # for each name of each file that has been found in this directory
        print(content_file_name)
        if content_file_name.replace(".txt","") == pgName: # if the name of this file is equal to the given pgName
            content_file = open(content_file_name,"r") # open this file as a file object
            if content_file != None: return content_file # if we can open this file, then return the file object

def getContent(pgName): # get the contents of a page
    this_page_content_file = findPage(pgName) # retrieve page contents for this file

    if this_page_content_file != None: # if the file holding this page's contents has been found...
        this_page_content = ""

        for line in this_page_content_file: # read a line from this file
            this_page_content += ""

        content_formatted = CONTENT.format(
            page_title="Index",
            page_content=this_page_content
        )

        return content_formatted
    else:
        return "<p>None</p>"


def getHeader():
    headerFormatted = HEADER.format(
        nav_links=getNavLinks(),
        header_image=getHeaderImage(),
        website_title=getWebsiteTitle()
    )

    return headerFormatted

def getFooter():
    footer_formatted = FOOTER.format(text="This is a footer")

    return footer_formatted

def drawStyling():
    print(STYLING)


def getNavLinks():
    str = ""

    for linkName in NAV_LINKS:
        str += "LINK STRING STUFF"
    str += ""

    return """<li><a href='#'>Home</a></li>
                    <li><a href='#'>Lifecycle</a></li>
                    <li><a href='#'>Conservation</a></li>"""  # DEFAULT 4 TESTING


def getHeaderImage():
    return "header.jpg"


def getWebsiteTitle():
    return "MichiganChinook"


def getPage(pgName): #getpagename, argument based on ending of page
    """
        works if you add:
                <py-script src="NAME_OF_PYTHON_FILE.py"></py-script>
            to webpage html fil
    """
    bodyStr = getStyling() + getHeader() + getContent(pgName) + getFooter()
    return bodyStr
