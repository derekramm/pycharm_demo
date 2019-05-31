#!/anaconda3/envs/env37/bin/python

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')
age = form.getvalue('age')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>cgi-get</title>")
print("</head>")
print("<body>")
print(f"<h2>name:{name}</h2>")
print(f"<h2>age:{age}</h2>")
print("</body>")
print("</html>")
