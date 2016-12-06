#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 4 - CSC210 Fall 2015
# Philip Guo

# To run, start AMPSS and visit URLs like the following to insert new
# entries into the database, then check your database's contents using
# lecture4-query-database.py
#
# http://localhost/cgi-bin/lecture4.py?my_name=Joe&my_age=32&my_image=../cat.jpg
# http://localhost/cgi-bin/lecture4.py?my_name=Donna&my_age=37&my_image=../dog.jpg

# useful for debugging
import cgitb
cgitb.enable()

import cgi
import sqlite3
import re
form = cgi.FieldStorage()

conn = sqlite3.connect('phoneContacts.db')
c = conn.cursor()
# insert new user data into the database

try:
    names = form['search'].value
    names = str(names)
    temporary = names
    names = re.split(', ', names)
    if len(names)==0:
        first_name = "empty"
        last_name ="empty"
    elif len(names)!=0 and len(names) > 1:
        first_name =names[0].title()
        last_name = names[1].title()
    else:
        temporary=temporary.split()
        if len(temporary)==1:
            first_name = temporary[0].title()
            last_name = temporary[0].title()
        else:
            first_name = temporary[0].title()
            last_name = temporary[1].title()
except KeyError:
    first_name = "empty"
    last_name ="empty"

c.execute("select FirstName from phone_contact where FirstName=?", (first_name,))
dataFN = c.fetchall()
c.execute("select LastName from phone_contact where LastName=?", (last_name,))
dataLN = c.fetchall()

# create a database file named 'people.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.

conn.commit()

import datetime
# print the http header
print ("Content-Type: text/html")
print # don't forget the extra newline

print ('<html>')
print (' <head>')
print ('<link rel="stylesheet" href="../HTML/assets/demo.css">')
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
# in Python, use ''' triple quotes ''' to create a multi-line string
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
            h3 {
            color: red;
            margin-top: 5%;
            margin-left: 27%;
            margin-bottom: 1%;
            }

		</style>
	</head>
''')
print ('	<body>')
print ('		<h2>')
#print (str(datetime.datetime.now()))
print ('		</h2>')

# print out the data for all users in the database
print '<table>'
print ('		<h3>These Contacts Below Matched One Of Your Criteria </h3>')
for row in c.execute('SELECT * FROM phone_contact;'):
    if dataFN and dataLN:
        if row[1] ==first_name.title() and row[2] ==last_name.title():
            print '<tr>{}</tr>'.format('  '.join(['<td>{}</td>'.format(col) for col in row]))
    elif dataFN or dataLN:
        if row[1] ==first_name.title() or row[2] ==last_name.title():
            print '<tr>{}</tr>'.format('  '.join(['<td>{}</td>'.format(col) for col in row]))
    elif len(first_name)==1 or len(last_name)==1:
        if row[1][0] ==first_name[0] or row[2][0] ==last_name[0]:
            print '<tr>{}</tr>'.format('  '.join(['<td>{}</td>'.format(col) for col in row]))

    #print '<tr>{}</tr>'.format(''.join(['<td>{}</td>'.format(col) for col in row]))

print '</table>'
conn.close()

print ('	</body>')
print ('</html>')
