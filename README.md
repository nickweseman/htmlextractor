# htmlextractor
Download and extract portions of websites in html format and package them up for epub conversion:

Using Python 3.

Steps:
1.  pip install beautifulsoup
2.  pip install lxml
3.  pip install requests
4.  Open up extractor.py:
      <li>update EPUB_NAME to be your desired epub name.
      <li>update URL and corresponding logic in parse() to fit your html site.
5.  python extractor.py
      This will generate a table of contents html file in the output/<ebook_name>/clean folder.
6.  Import the toc html file into Calibre (drag and drop)
      Download Calibre from https://calibre-ebook.com/
7.  Right click on the book in Calibre -> Convert books -> Convert individually.
8.  Output format = EPUB (or the format of your choice).  Click OK.
