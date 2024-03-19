import os
import sys

import pyscript
beginLayout = ""
endLayout = ""
STYLING = """
    <!-- Template CSS -->
    <link rel="stylesheet" href="styling.css"> <!-- Template stylesheet-->
    <!-- Bootstrap Icon CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
    """
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
    page_contents_list = os.listdir("../content/")

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
