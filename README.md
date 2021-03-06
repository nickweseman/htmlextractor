# htmlextractor + ebook packaging
This tool downloads and extracts portions of a website in html format and packages them up for epub conversion:

Using Python 3.

Steps:
1.  pip install beautifulsoup
2.  pip install lxml
3.  pip install requests
4.  Open up extractor.py:
      ```
      update EPUB_NAME to be your desired epub name.
      update URL and corresponding logic in parse() to fit your html site.
      ```
5.  python extractor.py
      ```
      This will generate a table of contents html file in the "output/<ebook_name>/clean" folder.
      ```
6.  Import the toc html file into Calibre via drag and drop
      ```
      Download Calibre from https://calibre-ebook.com/
      ```
7.  Right click on the book in Calibre -> Convert books -> Convert individually.
8.  Output format = EPUB (or the format of your choice).  Click OK.
