#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python

# Import necessary modules such as cgitb and cgi which enables us to run cgi apps and get data easily from forms
import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()
import sqlite3
import re
form = cgi.FieldStorage()

conn = sqlite3.connect('phoneContacts.db')
c = conn.cursor()


# Get values from the form such as the first_name, last_name, phone_number, email_address and message
# store this information in  variables
try:
    names = form['search'].value
    names = str(names)
    temporary = names
    names = re.split(', ', names)

    # If the user enters only one name such as the first name, assume the second name is empty
    if len(names)==0:
        first_name = "empty"
        last_name ="empty"
    elif len(names)!=0 and len(names) > 1:
        first_name =names[0].title()
        last_name = names[1].title()

    # If user enters only one letter of the name, assume the user thinks there is either a contact which is first_name or last_name
    #starts wth the supplied character and process the request as show further below
    else:
        temporary=temporary.split()
        if len(temporary)==1:
            first_name = temporary[0].title()
            last_name = temporary[0].title()
        else:
            first_name = temporary[0].title()
            last_name = temporary[1].title()
# This is to curb a user typing empty spaces as a name
except KeyError:
    first_name = "empty"
    last_name ="empty"

# Look if those entered names exist in the database
c.execute("select FirstName from phone_contact where FirstName=?", (first_name,))
dataFN = c.fetchall()
c.execute("select LastName from phone_contact where LastName=?", (last_name,))
dataLN = c.fetchall()


conn.commit()

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
print ('		</h2>')

# print out the data for all users in the database

print '<table>'
print ('		<h3>These Contacts Below Matched One Of Your Criteria </h3>')
for row in c.execute('SELECT * FROM phone_contact;'):
    # If the first_name and last_name are in the database, then display the Contacts information
    if dataFN and dataLN:
        if row[1] ==first_name.title() and row[2] ==last_name.title():
            print '<tr>{}</tr>'.format('  '.join(['<td>{}</td>'.format(col) for col in row]))
    # If only one of the names entered are in the database, display any contact whose first_name or last_name appears as entered
    elif dataFN or dataLN:
        if row[1] ==first_name.title() or row[2] ==last_name.title():
            print '<tr>{}</tr>'.format('  '.join(['<td>{}</td>'.format(col) for col in row]))

    # If the user just enters only one letter, display any contact whose first_name or last_name starts with such a letter
    elif len(first_name)==1 or len(last_name)==1:
        if row[1][0] ==first_name[0] or row[2][0] ==last_name[0]:
            print '<tr>{}</tr>'.format('  '.join(['<td>{}</td>'.format(col) for col in row]))


print '</table>'
conn.close()

print ('	</body>')
print ('</html>')
