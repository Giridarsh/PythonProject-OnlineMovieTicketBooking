#!/Python27/python.exe
print"content-type:text/html\n\r"
import MySQLdb
import cgi
db=MySQLdb.connect("127.0.0.1","root","root","movie",3306)
mycursor=db.cursor()
form=cgi.FieldStorage()
que="select email_id from temp"
mycursor.execute(que)
eque=mycursor.fetchone()
emailcheck=eque
##cemail_id=form.getvalue('em')
##cpassword=form.getvalue('password')
if db:
    view="select * from signupdb where email_id='%s'"%emailcheck
##    mycursor.execute(view)
    if(mycursor.execute(view)>0):
        
        print"<script>location.href='home.py'?email_id='%s'</script>"%emailcheck
##        print"<script>location.href='logintohome.py'</script>"
##        view="select * from signupdb where email_id='%s' and password='%s'"%(cemail_id,cpassword)
##    mycursor.execute(view)
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
       

print"""
<html>
<head><title>home</title>
<link rel='stylesheet' type='text/css' href='css.css'>
<script type='text/javascript' src='validate.js'></script>
</head>
<body>
<form name='page2' action='edit_store.py' method='post'>
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
</div></div>
<table border='0' width='100%'><td  align=center width='80%' font-color='white'><h1>TICKET MYSHOW</h1></td></tr>
</table>
"""
print"<div id=logintosignup>"
print"<div id=table><table border='0' cellpadding='3px' >"
print"<tr><td>Firstname:</td><td><input type='text' id='fname' name='fname' value= %s></td></tr>"%fname
print"<tr><td>lastname:</td><td><input type='text' id='lname' name='lname' value=%s></td></tr>"%lname
print"<tr><td>Country</td><td><input type='text' id='country' name='country' value=%s></td></tr>"%country
print"<tr><td>State</td><td><input type='text' id='state' name='state' value=%s></td></tr>"%state
print"<tr><td>City</td><td><input type='text' id='city' name='city' value=%s></td></tr>"%city
print"<tr><td>Pincode:</td><td><input type='text' id='pincode' name='pincode' value=%s></td></tr>"%pincode
print"<tr><td>E-mail Id:</td><td><input type='text' id='email' name='email' value=%s></td></tr>"%email_id
print"<tr><td>password:</td><td><input type='text' id='password' name='password' value=%s></td></tr>"%password
print"<tr><td>ph.no/mobile no:</td><td><input type='text' id='number' name='number' value=%s></td></tr>"%ph_no
print"<tr><td>Gender:</td><td><input type='text' id='gender' name='gender' value=%s></td></tr>"%gender
print"<tr><td>Address:</td><td><input type='text' id='addr' name='addr' value=%s></td></tr>"%address
print"""
<td ><input type='submit' name='save' value='save' id='save'></td></tr></table>
</div></div></div>
</form>
</body>
</html>"""


