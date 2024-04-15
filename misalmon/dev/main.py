import pyscript

STYLING = """
<!-- TEMPLATE CSS -->
    <link rel="stylesheet" href="../styling.css"> <!-- Template stylesheet-->
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
WEBSITE_TITLE = "MichiganChinook"
URL = "https://soleilector.github.io/misalmon/dev"
ROOT = "https://soleilector.github.io/misalmon"

paths = {
    "media" : "media/",
    "images" : "media/images/",
    "videos" : "media/videos/",
    "content" : "content/",
    "root" : "https://soleilector.github.io/misalmon/",
    "scripts" : "src/js",
    "styling" : "src/css",
    "url" : "https://soleilector.github.io/misalmon/dev/"
}

def setPath(pathName,pathPath):
    global paths
    paths[pathName] = pathPath

def getFileUrl(fileName,pathFolderName):
    return paths["root"] + paths[pathFolderName] + fileName

def transformPathKeys(str): # substitutes pathkeys with their associated paths
    newStr = str
    
    for pathName in paths:
    pathKey = "{"+pathName+"}"

    while pathKey in newStr: # continues to replace path keys of this value while it exists in this string
        pos = newStr.find(pathKey)
        
        # print(subKey)
        # print(pos)
        # print(newStr[pos:])
        
        beginning = newStr[:pos]  # # text before the path to be replaced
        ending = newStr[pos + len(pathKey):]  # text after the path to be replaced
        
        # print(beginning)
        # print(ending)

        fullPath = paths[root] + paths[pathName]
        newStr = beginning + fullPath + ending  # reform string with replaced path
        #print(newStr)
    
    return newStr

def formLink(page_name):
    return (page_name + WEBPAGE_EXTENSION)

def getStyling():
    return STYLING

def getScripts():
    return transformPathKeys("<script src='{scripts}dynamicPage.js'></script>")

def getContent(pgName): # get the contents of a page
    contentFormatted = ""
    
    if pgName in PAGE_CONTENT:
        thisContent = PAGE_CONTENT[pgName]
        
        contentFormatted = CONTENT.format(
            page_title = pgName,
            page_content = thisContent
        )
    else:
        contentFormatted = CONTENT.format(
            page_title = pgName,
            page_content = "<p>Nothing is written here</p>"
        )

    # begin changes
        contentFormatted = transformPathKeys(contentFormatted) + getScripts()
    # end changes
        
    return contentFormatted

def getHeader(temp_header=HEADER):
    headerFormatted = temp_header.format(
        nav_links=getNavLinks(),
        header_image=getHeaderImage(),
        website_title=getWebsiteTitle()
    )

    # begin changes
        headerFormatted = transformPathKeys(headerFormatted)
    # end changes

    return headerFormatted

def getFooter(temp_footer=FOOTER):
    footer_formatted = temp_footer.format(text="This is a footer")

    footer_formatted = transformPathKeys(footerFormatted)

    return footer_formatted

def getNavLinks(): # note: change to read from list later
    str = ""

    for linkName in NAV_LINKS:
        str += "LINK STRING STUFF"
    str += ""

    return """<li><a href='#'>Home</a></li>
                    <li><a href='#'>Lifecycle</a></li>
                    <li><a href='#'>Conservation</a></li>"""  # DEFAULT 4 TESTING


def getHeaderImage():
    #return "../media/images/header.jpg"
    return getFileUrl("header.jpg","images")


def getWebsiteTitle():
    return WEBSITE_TITLE

def capTitle(titleStr):
    words = titleStr.split(" ") # Split into a list, seperated by spaces
    newStr = "" # holds reconstructed string
    wordCt = 0 # counts words to identify which to add spaces after
    
    for word in words: # for each word in words array
        newStr += word[:1].upper() + word[1:] # capitalize first letter in the word
    
        wordCt += 1 # add word count
        if wordCt < len(words): # if the word of an id after this current word is not the last 
            newStr += " " # add a space to the reconstructed word
    
    return newStr

def getPage(pgName='Not Found'): #getpagename, argument based on ending of page
    """
        works if you add:
                <py-script src="NAME_OF_PYTHON_FILE.py"></py-script>
            to webpage html fil
    """
    
    bodyStr = getStyling() + getHeader() + getContent(pgName) + getFooter()
    return bodyStr

def pageFromContent(pgContent,pgName='index',temp_header=HEADER,temp_content=CONTENT,temp_footer=FOOTER):
    # capitalize first letter of page's name
    pgName = capTitle(pgName)
    
    # generate page's html
    content_formatted = temp_content.format(page_title=pgName,page_content=pgContent)
    header_formatted = getHeader(temp_header) # uses default static template embedded in file if no argument
    footer_formatted = getFooter(temp_footer) # uses default static template embedded in file if no argument
    print("AAAAGH")
    bodyStr = getStyling() + header_formatted + content_formatted + footer_formatted
    
    return bodyStr
    
