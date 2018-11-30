#!/usr/bin/env python3


import cgi, cgitb

import json

form = cgi.FieldStorage()

login = form.getvalue('login')
password = form.getvalue('password')


filename = login + ".json"


print('''
<!DOCTYPE html>

<html>
<head>
<title>Не о такой победе над Майкрософтом я мечтал</title>
<br>


</head>


<body style = "background-color:silver">''')


try:
	with open(filename, 'r') as file:
		data = json.loads(file.read())
		actualpassword = data['password']
		if password == actualpassword:
			string = 'Успех!'
		else:
			string = 'Неправильный пароль!'
except:
	string = 'Нет такого логина... Возможно, сначала надо зарегистрироваться?'

print('''
<!DOCTYPE html>

<html>
<head>
<title>Не о такой победе над Майкрософтом я мечтал</title>
<br>


</head>


<body style = "background-color:silver">
	<h1 align = "center" style = "color:steelblue">%s</h1> 


	






</body>

</html>
''' % (string))