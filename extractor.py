from bs4 import BeautifulSoup
import requests

# Note:  For Beautiful Soup, install the lxml parser.
# It works better than the default html.parser

# Pages:
# http://www.freevampires.net/young/yd6600.html
# http://www.freevampires.net/young/yd6600_2.html
# ...
# http://www.freevampires.net/young/yd6600_145.html

# Text inside a Page:
# <div class="text" align="justify">
# page text here
# </div>

URL = "http://www.freevampires.net/young/yd6600{}.html"

OUTPUT_BASE = "output/twilight_life_and_death"

OUTPUT_PATH = OUTPUT_BASE + "/raw/{}.html"
CLEAN_BASE = OUTPUT_BASE + "/clean"

CLEANED_OUTPUT_PATH = CLEAN_BASE + "/{}.html"
CLEANED_TOC = CLEAN_BASE + "/twilight_life_and_death_toc.html"

NUM_PAGES = 145

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


def download_and_parse():
    for page_num in range(1, NUM_PAGES + 1):
        if page_num == 1:
            response = requests.get(URL.format(""))
        else:
            response = requests.get(URL.format("_" + str(page_num)))

        with open(OUTPUT_PATH.format(page_num), "wb+") as f:
            f.write(response.content)
            parse(f, page_num)


def parse(f, page_num):
    f.seek(0)
    bsoup = BeautifulSoup(f, 'lxml')
    text = bsoup.find("div", class_="text").get_text()

    with open(CLEANED_OUTPUT_PATH.format(page_num), "wb") as clean_file:
        clean_file.write(str.encode(text))


def generate_toc():
    toc_html = [HEADER]

    for page_num in range(1, NUM_PAGES + 1):
        toc_html.append("\t\t\t<a href='{}.html'>File {}</a><br/>\n".format(
            page_num, page_num))

    toc_html.append(FOOTER)

    with open(CLEANED_TOC, "w") as f:
        f.write("".join(toc_html))


def main():
    download_and_parse()
    generate_toc()

if __name__ == "__main__":
    main()
