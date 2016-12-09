#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python

# Import necessary modules such as cgitb and cgi which enables us to run cgi apps and get data easily from forms
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

# Get values from the form such as the first_name, last_name, phone_number, email_address and message
# store this information in  variables
first_name = form['first_name'].value.title()
last_name = form['last_name'].value.title()
new_first_name = form['new_first_name'].value.title()
new_last_name = form['new_last_name'].value.title()
import sqlite3

# Connect to a database
conn = sqlite3.connect('phoneContacts.db')
c = conn.cursor()

# Check if the entered first_name and last_name are in the database yet.
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

# Make a easy navigation to go back to the main menu
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


#Use the CSS attributes to style up the file
print ('''
			h1, h2 {
				font-size: 100px;
				font-family: arial;
                margin-left: 35%;
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

# If the last_name and first_name exists in the database, then update the contacts name
if dataFN and dataLN:
    c.execute('''UPDATE phone_contact SET FirstName = ? WHERE LastName = ? ''', (new_first_name, last_name))
    c.execute('''UPDATE phone_contact SET LastName = ? WHERE FirstName = ? ''', (new_last_name, new_first_name))
    print ('<h3> Renamed Contact ' + first_name + "  " + last_name + "  to " + new_first_name + "  " + new_last_name +' on ' +  str(datetime.datetime.now()) + '</h3>')
# Else let the user know that such names are not in the database
else:
    print ('<h3> The contact with name ' + first_name + "  " + last_name +' does not exists ' + str(datetime.datetime.now())+ '</h3>')
conn.commit()
print ('	<body>')
print ('		</h2>')

conn.close()
print ('	</body>')
print ('</html>')
