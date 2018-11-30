#!/usr/bin/env python3




print('''
<!DOCTYPE html>

<html>
<head>
<title>Взод в Матрицу</title>
<br>


</head>


<body style = "background-color:silver">
	<h1 align = "center" style = "color:steelblue">Введите, пожалуйста, свои логин и пароль</h1> 


	
	<form action = "/cgi-bin/social.py" method = "post" >
	<center>
	Логин: <input type = "text" name = "login"> <br/>
	Пароль: <input type = "text" name = "password"> <br/>
	<input type = "submit" value = "Готово!" />
	</center>
	</form>





</body>

</html>
''')