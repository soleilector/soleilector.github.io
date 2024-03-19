import pyscript

STYLING = """
<!-- TEMPLATE CSS -->
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
    "Home": "home_py.html",
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
PAGE_CONTENT = {
    "index" : """<p>This is some content. Maybe you should go ahead and
                click this <button>in-text button</button> to see what it does.</p>
            <button>Click Me!</button><br>
            <h3>Centered buttons</h3>
            <p>The below <i>div</i> displays a row of 3 centered buttons...</p>
            <div class="btnCntr">
                <button>BTN</button>
                <button>BTN</button>
                <button>BTN</button>
            </div>
            <table class="general">
                <tr>
                    <th colspan="3">
                        Table Heading
                    </th>
                </tr>
                <tr>
                    <td>Row 1</td>
                    <td>Row 2</td>
                    <td>Row 3</td>
                </tr>
            </table>"""
}
FOOTER = """
<footer> <!-- BEGIN FOOTER -->
        <p>{text}</p>
    </footer> <!-- END FOOTER -->
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
    if "pgName" in PAGE_CONTENT:
        thisContent = PAGE_CONTENT[pgName]
        
        contentFormatted = CONTENT.format(
            page_title="Index",
            page_content = thisContent
        )
    else: return "<p>Nothing is written here...</p>"

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

def pageFromContent(pgContent):
    pgName = 'index'
    print(pgContent)
    bodyStr = getStyling() + getHeader() + CONTENT.format(page_title=pgName, page_content=pgContent) + getFooter()
    print("BODY FULL")
    print(bodyStr)
    return bodyStr
    
