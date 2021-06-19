#!/Python27/python.exe
print"content-type:text/html\n\r"
import MySQLdb
import cgi
print"""
<html>
<head><title>Signup</title>
<link rel='stylesheet' type='text/css' href='css.css'>
<script type='text/javascript' src='validate.js'></script>
</head>
<body>
<form name='reg' action='store_signup.py' method='post' enctype='multipart/form-data'>
<div id='page1'>
<center>
<table border='0' width='100%'><tr><td  align=center width='80%'><h1><font color='white'>TICKET MYSHOW</h1></td></tr></table>
<div id=table><table border='0' cellpadding='5px' >
<tr><td><font color='white'>Firstname:</td><td><input type='text'  name='fname' id='fname'></td></tr>
<tr><td><font color='white'>lastname:</td><td><input type='text'  name='lname' id='lname'></td></tr>
<tr><td><font color='white'>Country</td><td><select name='country' id='country' onChange='cstate();'>
<option value='0'>--select--
<option value='india'>india
<option value='pak'>pak
<option value='USA'>USA</select></td></tr>
<tr><td><font color='white'>State</td><td><select name='state' id='state' onChange='ccity();' disabled>
<option value='0'>--select--
<option value='Tamilnadu'>Tamilnadu
<option value='kerla'>kerla
<option value='karnataga'>karnataga
</select></td></tr>
<tr><td><font color='white'>City</td><td><select name='city' id='city' onchange='return emptycity();' disabled>
<option value='0'>--select--
<option value='coimbatore'>coimbatore
<option value='madurai'>madurai
<option value='virudhunagar'>virudhunagar
<option value='vellor'>vellor
<option value='chennai'>chennai
</select></td></tr>
<tr><td><font color='white'>Pincode:</td><td><input type='text' name='pincode' maxlength='6' id='pincode' onkeypress='return isnumber(event,this);'></td></tr>
<tr><td><font color='white'>E-mail Id:</td><td><input type='text' name='em'  id='em' onblur='return emailcheck();'></td></tr>
<tr><td><font color='white'>password:</td><td><input type='password' name='password' id='password'></td></tr>
<tr><td><font color='white'>ph.no/mobile no:</td><td><input type='text' name='number' maxlength='10' id='number' onkeypress='return checkno(event,this);'></td></tr>
<tr><td><font color='white'>Gender:</td><td><input type='radio' name='gender' value='male' id='gender' ><font color='white'>male
<input type='radio' name='gender' value='female'><font color='white'>female</td></tr>
<tr><td><font color='white'>Address:</td><td><textarea name='addr' id='addr' rows=5 cols=20 ></textarea></td></tr>
<tr><td><input type='reset' name='reset' id='reset'></td>
<td ><input type='submit' name='sub' value='signup' id='signup' onclick='return valid();' ></td></tr></table>
</div></div>
</center>
</form>
</body>
</html>
"""


