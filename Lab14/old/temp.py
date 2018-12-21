#!/usr/bin/env python3


import cgi, cgitb

import json

form = cgi.FieldStorage()

login = form.getvalue('login')

filename = login + ".json"


try:
	with open(filename, 'r') as file:
		string = "Файл найден"
except:
	string = 'Файла нет'

print('''
<!DOCTYPE html>

<html>
<head>
<title>Бросить всё и уехать в Урюпинск</title>
<br>


</head>


<body style = "background-color:silver">
	<h1 align = "center" style = "color:steelblue">%s</h1> 
	
	<form action = "/cgi-bin/social.py" method = "post" >
		<center>
		Чьи посты Вас интересуют? <br>
		<input type = "text" name = "login"> <br/>
		<input type = "submit" value = "Найти" />
		</center>
	</form>

	






</body>

</html>
''' % (string))
