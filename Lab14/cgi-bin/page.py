#!/usr/bin/env python3

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
<h1 align = "center" style = "color:steelblue">Привет</h1> 

<hr>

<p style ="font-family:Calibri; font-size: 200%">ААААААААААААААААААААА</p>
<p style ="font-family:Comic Sans MS; font-size: 150%">Самый лучший шрифт</p>
<p style ="font-style: italic">Курсив</p>
<p><i>Ещё курсив</i></p>
<p style = "background-color:green">Выделение цветом</p>
<p><span style = "background-color:green">Ещё выделение цветом</span></p>
<p><mark>Третье выделение цветом</mark></p>
<p><del>Зачёркивание</del></p>

<p><abbr title = "Новосибирский Государственный Университет">НГУ</abbr> круто <br>
<address><a href = "another.html">Типа адрес</a></address> <br>
<bdo dir = "rtl">привет</bdo></p>


<p style ="border:5px solid #3cb372" align = "center">Тут могла быть ваша реклама.</p>
<br><br><br>
<a href = "another.html">Не нажимать</a>
<p align = "center"><img src = "cat.jpg" width = "320" height = "180"></img></p>
<p align = "center"><i>Кот</i></p>
<br><br><br>

<table>
	<tr>
		<th>Имя</th>
		<th>Фамилия</th>
	</tr>
	<tr>
		<th>Иван</th>
		<th>Иванов</th>
	</tr>
	<tr>
		<th>Петр</th>
		<th>Петров</th>
	</tr>
</table>

</body>

</html>
''')