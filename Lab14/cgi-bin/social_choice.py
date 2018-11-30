#!/usr/bin/env python3





print('''
<!DOCTYPE html>

<html>
<head>
<title>Куды крестьянину подасться?</title>
<br>
<title></title>

</head>


<body style = "background-color:silver">
	<h1 align = "center" style = "color:steelblue">Добро пожаловать!</h1> 
	<h1 align = "center" style = "color:green">Пожалуйста, войдите в систему</h1> 


	
	<form action = "/cgi-bin/social_login.py" method = "post" >
	<center>
	<input type = "submit" value = "Войти!">
	</center>
	</form>
	
	
	<form action = "/cgi-bin/social_register.py" method = "post ">
	<center>
	<input type = "submit" value = "Зарегистрироваться!">
	</center>
	</form>
	
	<form action = "/cgi-bin/social_getmessages.py" method = "post ">
	<center>
	<input type = "submit" value = "Что пишут?">
	</center>
	</form>





</body>

</html>
''')