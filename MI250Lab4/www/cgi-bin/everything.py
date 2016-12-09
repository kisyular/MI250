#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python

# Import necessary modules such as cgitb and cgi which enables us to run cgi apps and get data easily from forms
import cgitb
cgitb.enable()

import cgi
import re
form = cgi.FieldStorage()


import sqlite3
conn = sqlite3.connect('phoneContacts.db')
c = conn.cursor()

conn.commit()

import datetime


# print the http header
print ("Content-Type: text/html")
print # don't forget the extra newline

print ('<html>')
print (' <head>')
print ('<link rel="stylesheet" href="../HTML/assets/demo.css">')

# Display a navigation menu
print ('''<ul>
    <li><a href="../index.html">HOME</a></li>
    <li><a href="../HTML/form-add.html">ADD CONTACT</a></li>
    <li><a href="../HTML/form-display-everything.html">DISPLAY PHONE BOOK</a></li>
    <li><a href="../HTML/form-update.html">UPDATE CONTACT</a></li>
    <li><a href="../HTML/form-search.html">SEARCH CONTACT</a></li>
    <li><a href="../HTML/form-delete-contact.html">DELETE CONTACT</a></li>
</ul>''')
print ('		<title>')
print ('			PHONE BOOK DIRECTORY')
print ('		</title>')
print ('		<style type="text/css">')
# Use custom style from css to style the html file
print ('''
			h1 {
				font-size: 100px;
				font-family: arial;
			}
			img {
				width: 300px;
			}
			p#myLine {
				color: red;
			}
            table, th, td {
            border: 1px solid black;
            margin-left: 20%;
            }
            td, tr{
            padding:10px 10px 0 1%;
            color: aqua;
            background-color: black;
            }
            h2 {
            margin-left: 45%;
            }
            h3 {
            color: red;
            margin-top: 1%;
            margin-left: 25%;
            margin-bottom: 1%;
            }

		</style>
	</head>
''')
print ('	<body>')
print ('		<h3>These  are Contacts In Your Phone Book Directory </h3>')
print ('		<h2>')

#print (str(datetime.datetime.now()))
print ('		</h2>')

# print out the data for all users in the database
print '<table>'

for row in c.execute('SELECT * FROM phone_contact;'):
    print '<tr>{}</tr>'.format('  '.join(['<td>{}</td>'.format(col) for col in row]))

print '</table>'
conn.close()

print ('	</body>')
print ('</html>')
