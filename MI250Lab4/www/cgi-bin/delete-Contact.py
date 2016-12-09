#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python

# Import necessary modules such as cgitb and cgi which enables us to run cgi apps and get data easily from forms
import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()

# Get values from the form submitted
first_name = form['first_name'].value.title()
last_name = form['last_name'].value.title()

# Import sqlite
import sqlite3

# Check if the first_name or last_name are in the sqlite3 database
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
print ('		<h2>PHONE BOOK</h2>')

# If the last_name and first_name exists in the database, then delete the contact
if dataFN and  dataLN:
    c.execute('''DELETE FROM phone_contact WHERE FirstName = ? ''', (first_name,))
    print ('<h3> Deleted Contact ' + first_name + "  " + last_name +' on ' +  str(datetime.datetime.now()) + '</h3>')

# Else let the user know that such names are not in the database
else:
    print ('<h3> The contact with name ' + first_name + "  " + last_name +' does not exists ' + str(datetime.datetime.now())+ '</h3>')
conn.commit()
print ('	<body>')
print ('		</h2>')
conn.close()
print ('	</body>')
print ('</html>')
