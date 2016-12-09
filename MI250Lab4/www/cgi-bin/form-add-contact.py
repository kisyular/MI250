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
phone_number = form['phone_number'].value
email_address = form['email_address'].value
message = form['message'].value.title()

# Connect to a database
import sqlite3
# create a database file named 'phoneContacts.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.
conn = sqlite3.connect('phoneContacts.db')
c = conn.cursor()

# Create a table in the database if the table does not exist yet
c.execute('create table if not exists phone_contact(ID INTEGER PRIMARY KEY, FirstName varchar(100), LastName varchar(100), PhoneNumber integer, Email varchar(100), Message varchar(200), Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')

# Check if the entered first_name and last_name are in the database yet.
# This is to avoid multiple people sharing the same first_name and last_name
# THis means they can share either first_name or last_name but not them at once
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
            margin-left: 35%;
            margin-bottom: 1%;
            }

		</style>
	</head>
''')
print ('		<h2>PHONE BOOK</h2>')

# If the person does not exist in the database then we add then. Else, we let the user know such contact is already in the database
if not dataFN or not dataLN:
    c.execute('insert into phone_contact(FirstName, LastName, PhoneNumber, Email, Message) values (?,?,?,?,?)', (first_name, last_name, phone_number, email_address, message))
    print ('<h3> New contact ' + first_name + "  " + last_name +'  created on ' +  str(datetime.datetime.now()) + '</h3>')
else:
    print ('<h3> The contact with name ' + first_name + "  " + last_name +' already exists <br/><br/>' + str(datetime.datetime.now())+ '</h3>')
conn.commit()
print ('	<body>')
print ('		</h2>')
conn.close()
print ('	</body>')
print ('</html>')
