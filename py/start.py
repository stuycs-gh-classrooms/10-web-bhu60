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
name = 'Your Name'
if ('name' in data):
    name = data['name'].value
guide = 'Chiron'
if ('guide' in data):
    bgcolor = data['bgcolor'].value

html= HTML_HEADER
html+= '<h1>Welcome to Camp-Half-Blood ' + name + '</h1>'
html+= '<br><a href="start.html">Try Again</a>'
html+= HTML_FOOTER
print(html)