#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Welcome to Camp-Half-Blood</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""


data = cgi.FieldStorage()

if 'option' in data:
    page = data['option'].value
else:
    page = 'none'

html= HTML_HEADER
html+= '<br><a href="' + str(page) + '.html">yay</a>'
html+= HTML_FOOTER
print(html)
