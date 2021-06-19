#!/Python27/python.exe
print"content-type:text/html\n\r"
import MySQLdb
import cgi
db=MySQLdb.connect("127.0.0.1","root","root","movie",3306)
mycursor=db.cursor()
form=cgi.FieldStorage()
fetch="select email_id from temp"
mycursor.execute(fetch)
emailf=mycursor.fetchone()
email=emailf
view="select * from signupdb where email_id='%s'"%email
if(mycursor.execute(view)>0):
    res=mycursor.fetchall()
    for a in res:
        fname=a[0]
        lname=a[1]
        country=a[2]
        state=a[3]
        city=a[4]
        pincode=a[5]
        email_id=a[6]
        ph_no=a[7]
        gender=a[8]
        address=a[9]
        password=a[10]
else:
    print"""<li>user email/password is incorrect</li>
<li>
<a href='tempdel.py'>Home</a>
</li>"""
    
       

print"""
<html>
<head><title>home</title>
<link rel='stylesheet' type='text/css' href='css.css'>
<script type='text/javascript' src='validate.js'></script>
</head>
<body>
<form name='page2' action='tempdel.py' method='post'>
<div id='logintobg'>
<div id='click'>
<li>
<a href='index.py'>Home</a>
</li>
<li><a href='movie_list.py'>All movie</a>
</li>
<li><a href='#'>Ticket booking</a>
</li>
<li><a href='login.py'>login</a>
</li>
<li><a href='signup.py'>Signup</a>
</li>
<li><a href='#'>contact</a>
</li>
</div>
<table border='0' width='100%'>
<tr><td  align=center width='80%' font-color='white'><h1>TICKET MYSHOW</h1></td></tr></table>
"""
print"<div id=logintosignup>"
print"<div id=table><table border='0' cellpadding='3px' >"
print"<tr><td>Firstname:</td><td>%s</td></tr>"%fname
print"<tr><td>lastname:</td><td>%s</td></tr>"%lname
print"<tr><td>Country</td><td>%s</td></tr>"%country
print"<tr><td>State</td><td>%s</td></tr>"%state
print"<tr><td>City</td><td>%s</td></tr>"%city
print"<tr><td>Pincode:</td><td>%s</td></tr>"%pincode
print"<tr><td>E-mail Id:</td><td>%s</td></tr>"%email_id
print"<tr><td>password:</td><td>%s</td></tr>"%password
print"<tr><td>ph.no/mobile no:</td><td>%s</td></tr>"%ph_no
print"<tr><td>Gender:</td><td>%s</td></tr>"%gender
print"<tr><td>Address:</td><td>%s</td></tr>"%address
print"""
<tr><td><input type='submit'  name='edit' id='edit' value='edit' formaction='edit.py' ></td>
<td ><input type='submit' name='logout' value='logout' id='logout'></td></tr></table>
</div></div></div>
</form>
</body>
</html>"""


