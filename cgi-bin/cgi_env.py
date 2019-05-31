#!/anaconda3/envs/env37/bin/python

import os

print('Content-type: text/html')
print()
print('<meta charset="utf-8">')
print("<h2>环境变量</h2>")
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span> : %s </li>" % (key, os.environ[key]))
print("</ul>")
