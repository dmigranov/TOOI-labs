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


''')


try:
	with open(filename, 'r') as file:
		data = json.loads(file.read())
		actualpassword = data['password']
		if password == actualpassword:
			message = form.getvalue('message')
			if message != None:
				data['messages'].append({"message" : message})
				with open(filename, 'w') as file:
					json.dump(data, file)
			print('''
			<body style = "background-color:silver">
			<form action = "/cgi-bin/social.py" method = "post" >
			<center>
			<input type = "text" name = "message"> <br/>
			<input type = "hidden" name = "login" value = %s>
			<input type = "hidden" name = "password" value = %s>
			<input type = "submit" value = "Запостить" />
			</center>
			</form>
			<br>
			<br>
			''' % (login, password))
			
			
			for message in data['messages']:
				print('''
				%s <br>
				<br>
				''' %(message['message']))
		else:
			print('''
			<body style = "background-color:silver">
			<h1 align = "center" style = "color:steelblue">Неправильный пароль</h1> 
			''')
except:

	print('''
	<body style = "background-color:silver">
	<h1 align = "center" style = "color:steelblue">Нет такого логина... Возможно, сначала надо зарегистрироваться?</h1> 
	''')

print('''



	

</body>

</html>
''')
