#!/usr/bin/env python3


import cgi, cgitb

import json

form = cgi.FieldStorage()

login = form.getvalue('login')
password = form.getvalue('password')

filename = login + ".json"


try:
	with open(filename, 'r') as file:
		string = "Имя уже занято..."
except:
	with open(filename, 'w', encoding = 'utf-8') as file:
		jsonstring = json.dumps({"password" : password, "messages" : []})
		file.write(jsonstring)
		string = 'Успех! Теперь Вы можете залогиниться'

print('''
<!DOCTYPE html>

<html>
<head>
<title>Регистрация</title>
<br>


</head>


<body style = "background-color:silver">
	<h1 align = "center" style = "color:steelblue">%s</h1> 


	






</body>

</html>
''' % (string))