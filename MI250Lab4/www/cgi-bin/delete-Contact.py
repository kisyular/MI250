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
form = cgi.FieldStorage()

first_name = form['first_name'].value.title()
last_name = form['last_name'].value.title()


# insert new user data into the database
import sqlite3
# create a database file named 'people.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.
conn = sqlite3.connect('phoneContacts.db')
c = conn.cursor()
c.execute("select FirstName from phone_contact where FirstName=?", (first_name,))
dataFN = c.fetchall()
c.execute("select LastName from phone_contact where LastName=?", (last_name,))
dataLN = c.fetchall()
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
            h1, h2 {
				font-size: 100px;
				font-family: arial;
                margin-left: 30%;
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
            margin-left: 35%;
            margin-bottom: 1%;
            }

		</style>
	</head>
''')
print ('		<h2>PHONE BOOK</h2>')
if dataFN and  dataLN:
    c.execute('''DELETE FROM phone_contact WHERE FirstName = ? ''', (first_name,))
    print ('<h3> Deleted Contact ' + first_name + "  " + last_name +' on ' +  str(datetime.datetime.now()) + '</h3>')
else:
    print ('<h3> The contact with name ' + first_name + "  " + last_name +' does not exists ' + str(datetime.datetime.now())+ '</h3>')
conn.commit()
print ('	<body>')
print ('		</h2>')
conn.close()
print ('	</body>')
print ('</html>')
