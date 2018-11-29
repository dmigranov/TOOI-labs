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
	<h1 align = "center" style = "color:green">Вы уже зарегистрированы?</h1> 


	
	<form action = "/cgi-bin/social_login.py" method = "post" >
	<center>
	<input type = "submit" value = "Да!"">
	</center>
	</form>

	<form action = "/cgi-bin/social_register.py" method = "post"">
	<center>
	<input type = "submit" value ="Пока нет"">
	</center>
	</form>



</body>

</html>
''')