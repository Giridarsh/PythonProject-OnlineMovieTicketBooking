#!/Python27/python.exe
import MySQLdb
import cgi
print"content-type:text/html\n\r"
print"""<html>
<head>
<title>login</title>
<link rel='stylesheet' type='text/css' href='css.css'>
<script type='text/javascript' src='validate.js'></script>
</head>
<body>
<form name='login' action='tempdb.py' method='post'>
<div id='page'>
<table border='0' align='center' cellspacing='55px' cellpadding='10px'>
<tr><td  align=center width='80%' font-color='white'><h1><font color='white'>TICKET MYSHOW</font></h1></td></tr></table>
<table align='center'  cellspacing='45px' cellpadding='0px' >
<tr><td><strong><font color='white'>Email-id:</font></strong></td><td><input type='text' name='em' id='em'onblur='return emailcheck();' ></td></tr>
<tr><td><strong><font color='white'>password:</font></strong></td><td><input type='password' name='password' id='password'></td></tr>
<tr><td align=center><input type='submit' name='login' value='login' id='login' onclick='return clogin();'></td></tr>
</table></div>
</div>
</form>
</body>
</html>"""
