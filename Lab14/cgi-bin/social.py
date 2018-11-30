#!/usr/bin/env python3


import cgi, cgitb

form = cgi.FieldStorage()

login = form.getvalue('login')
password = form.getvalue('password')


print('''
<!DOCTYPE html>

<html>
<head>
<title>Взод в Матрицу</title>
<br>


</head>


<body style = "background-color:silver">
	<h1 align = "center" style = "color:steelblue">%s %s</h1> 


	






</body>

</html>
''' % (login, password))