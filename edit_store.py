#!/Python27/python.exe
print"content-type:text/html\n\r"
import MySQLdb
import cgi
db=MySQLdb.connect("127.0.0.1","root","root","movie",3306)
mycursor=db.cursor()
form=cgi.FieldStorage()
lname=form.getvalue('lname')
name=form.getvalue('fname')
country=form.getvalue('country')
state=form.getvalue('state')
city=form.getvalue('city')
pincode=form.getvalue('pincode')
email_id=form.getvalue('email')
ph_no=form.getvalue('number')
gender=form.getvalue('gender')
address=form.getvalue('addr')
password=form.getvalue('password')
que="select email_id from temp"
mycursor.execute(que)
eque=mycursor.fetchone()
emailcheck=eque 
query="update signupdb set first_name='%s',last_name='%s',country='%s',state='%s',city='%s',pincode='%s',email_id='%s',ph_no='%s',gender='%s',address='%s',password='%s'"%(name,lname,country,state,city,pincode,email_id,ph_no,gender,address,password)
mycursor.execute(query)
db.commit()
print"<script language=javascript>location.href='login_store.py';</script>"
