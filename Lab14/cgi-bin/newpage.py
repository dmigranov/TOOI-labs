#!/usr/bin/env python3

import cgi, cgitb

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')


print('''
<!DOCTYPE html>

<html>
<head>
<title>Йоу</title>
<style>
table, th, td {
	border: 2px solid black;
	border-collapse: collapse;

}
</style>
</head>


<body style = "background-color:silver">
<h1 align = "center" style = "color:steelblue">Привет %s %s</h1> 

<form action = "/cgi-bin/newpage.py" method = "post">
First Name: <input type = "text" name = "first_name"> <br/>
Last Name: <input type = "text" name = "last_name"> <br/>
Checkbox: <input type = "checkbox"> <br/>
Radio: <input name="group1" type="radio" />
<input type = "submit" value = "Submit" />
</form>

</body>

</html>
''' % (first_name, last_name) )