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
email_id=form.getvalue('em')
ph_no=form.getvalue('number')
gender=form.getvalue('gender')
address=form.getvalue('addr')
password=form.getvalue('password')
if db:
##    lname=form.getvalue('lname')
##    name=form.getvalue('fname')
##    country=form.getvalue('country')
##    state=form.getvalue('state')
##    city=form.getvalue('city')
##    pincode=form.getvalue('pincode')
##    email_id=form.getvalue('em')
##    ph_no=form.getvalue('number')
##    gender=form.getvalue('gender')
##    address=form.getvalue('addr')
##    interseted_in=form.getvalue('a[]')
    print email_id
    que="INSERT INTO signupdb (first_name,last_name,country,state,city,pincode,email_id,ph_no,gender,address,password) VALUES ('%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s')"%(name,lname,country,state,city,pincode,email_id,ph_no,gender,address,password)
    mycursor.execute(que)
    db.commit()
else:
    print"error"
cemail_id=form.getvalue('em')
cpassword=form.getvalue('password')
if db:
    view="select * from signupdb where email_id='%s' and password='%s'"%(cemail_id,cpassword)
    mycursor.execute(view)
    print "<script>location.href='index.py'</script>"
else:
    print "failed"