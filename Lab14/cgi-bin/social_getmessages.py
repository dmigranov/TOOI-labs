#!/usr/bin/env python3


import cgi, cgitb

import json

form = cgi.FieldStorage()

login = form.getvalue('login')





print('''
<!DOCTYPE html>

<html>
<head>
<title>Бросить всё и уехать в Урюпинск</title>
<br>


</head>


<body style = "background-color:silver"><h1 align = "center" style = "color:steelblue">Найти посты пользователя</h1> 
	
	<form action = "/cgi-bin/social_getmessages.py" method = "post" >
		<center>
		Чьи посты Вас интересуют? <br> <br>
		<input type = "text" name = "login"> <br/>
		<input type = "submit" value = "Найти" />
		</center>
	</form>

	''')


if login != None:
	filename = login + ".json"
	try:
		with open(filename, 'r') as file:
			data = json.loads(file.read())
			string = "Посты пользователя " + login
			print('''
			
			
			
			<h1 align = "center" style = "color:steelblue">%s</h1>''' % string)
			
			for message in data['messages']:
				print('''
				%s <br>
				<br>
				''' %(message['message']))
			
	except:
		print('''
			
			
			
			<h1 align = "center" style = "color:steelblue">Такого пользователя нет</h1>''')
else:
	print('''
			
			
			
			<h1 align = "center" style = "color:steelblue">Введите ник требуемого пользователя</h1>''')



print('''
</body>

</html>
''')