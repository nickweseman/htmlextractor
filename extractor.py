import os

import requests
from bs4 import BeautifulSoup

# Note:  For Beautiful Soup, install the lxml parser.
# It works better than the default html.parser

#####################################################
# Update these variables to fit your use case

# Example Input:
# Pages:
# http://www.freevampires.net/young/yd6600.html
# http://www.freevampires.net/young/yd6600_2.html
# ...
# http://www.freevampires.net/young/yd6600_145.html
URL = "http://www.freevampires.net/young/yd6600{}.html"  # also update parse()
NUM_PAGES = 145

EPUB_NAME = "twilight_life_and_death"
#####################################################

OUTPUT_DIR = "output"
EPUB_DIR = OUTPUT_DIR + "/" + EPUB_NAME

RAW_DIR = EPUB_DIR + "/raw"
RAW_FILEPATH = RAW_DIR + "/{}.html"

CLEAN_DIR = EPUB_DIR + "/clean"
CLEAN_FILEPATH = CLEAN_DIR + "/{}.html"
CLEAN_TOC_FILEPATH = CLEAN_DIR + "/" + EPUB_NAME + "toc.html"

HEADER = """
<html>
    <body>
        <h1>Table of Contents</h1>
        <p style='text-indent:0pt'>
"""

FOOTER = """
        </p>
    </body>
</html>
"""


def create_output_folders():
    folders = [OUTPUT_DIR, EPUB_DIR, RAW_DIR, CLEAN_DIR]

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)


def download_and_parse():
    create_output_folders()

    for page_num in range(1, NUM_PAGES + 1):
        if page_num == 1:
            response = requests.get(URL.format(""))
        else:
            response = requests.get(URL.format("_" + str(page_num)))

        with open(RAW_FILEPATH.format(page_num), "wb+") as f:
            f.write(response.content)
            parse(f, page_num)


# e.g. Text inside a Page looks like this:
# <div class="text" align="justify">
# page text here
# </div>

def parse(f, page_num):
    f.seek(0)

    bsoup = BeautifulSoup(f, 'lxml')
    text = bsoup.find("div", class_="text").get_text()

    with open(CLEAN_FILEPATH.format(page_num), "wb") as clean_file:
        clean_file.write(str.encode(text))


def generate_toc():
    toc_html = [HEADER]

    for page_num in range(1, NUM_PAGES + 1):
        toc_html.append("\t\t\t<a href='{}.html'>File {}</a><br/>\n".format(
            page_num, page_num))

    toc_html.append(FOOTER)

    with open(CLEAN_TOC_FILEPATH, "w") as f:
        f.write("".join(toc_html))


def main():
    download_and_parse()
    generate_toc()

if __name__ == "__main__":
    main()
