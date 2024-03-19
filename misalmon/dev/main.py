import pyscript

beginLayout = ""
endLayout = ""
STYLING = """
    """
HEADER = """<header>
    </header>"""
NAV_LINKS = {
}
CONTENT = """
"""
FOOTER = """
"""
WEBPAGE_EXTENSION = "html"
HEADER_IMAGE = "header.jpg"
WEBSITE_TITLE = "MichiganSalmon"
URL = "https://soleilector.github.io/misalmon/dev"
CONTENT_URL = "https://soleilector.github.io/misalmon/content/"

def formLink(page_name):
    return (page_name + WEBPAGE_EXTENSION)

def getStyling():
    return STYLING

def getContent(pgName): # get the contents of a page
    page_content = ""
    that  = fetch(CONTENT_URL+pgName+".txt")
    print("COME HERE===>>"+str(that))
    
    return "<p>Nothing is written here...</p>"

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
