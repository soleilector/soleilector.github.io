import pyscript

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
FOOTER = """
<footer> <!-- BEGIN FOOTER -->
        <p>{text}</p>
    </footer> <!-- END FOOTER -->
"""

WEBPAGE_EXTENSION = "html"
HEADER_IMAGE = "../media/images/header.jpg"
WEBSITE_TITLE = "MichiganChinook"


def formLink(page_name):
    extension = WEBPAGE_EXTENSION

    if WEBPAGE_EXTENSION != None and WEBPAGE_EXTENSION != "":
        extension = "." + WEBPAGE_EXTENSION

    return (page_name + extension)

def getStyling():
    return """
    <!-- TEMPLATE CSS -->
        <link rel="stylesheet" href="styling.css"> <!-- Template stylesheet-->
        <!-- Bootstrap Icon CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
    """

def getContent():
    content_formatted = CONTENT.format(
        page_title="Index",
        page_content="""<p>This is some content. Maybe you should go ahead and
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
    )

    return content_formatted


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

def getNavLinks():
    str = ""

    for linkName in NAV_LINKS:
        str += "LINK STRING STUFF"
    str += ""

    return """<li><a href='#'>Home</a></li>
                    <li><a href='#'>Lifecycle</a></li>
                    <li><a href='#'>Conservation</a></li>"""  # DEFAULT 4 TESTING


def getHeaderImage():
    return HEADER_IMAGE


def getWebsiteTitle():
    return WEBSITE_TITLE


def getPage(): #getpagename, argument based on ending of page
    """
        works if you add:
                <py-script src="NAME_OF_PYTHON_FILE.py"></py-script>
            to webpage html fil
    """
    bodyStr = getStyling() + getHeader() + getContent() + getFooter()
    return bodyStr
