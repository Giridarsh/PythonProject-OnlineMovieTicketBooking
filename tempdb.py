#!/Python27/python.exe
print"content-type:text/html\n\r"
import MySQLdb
import  cgi
db=MySQLdb.connect("127.0.0.1","root","root","movie",3306)
mycursor=db.cursor()
form=cgi.FieldStorage()
cemail_id=form.getvalue('em')
cpassword=form.getvalue('password')
if db:
    view="select * from signupdb where email_id='%s' and password='%s'"%(cemail_id,cpassword)
    mycursor.execute(view)
    if(view>0):
        insert="insert into temp values('%s','%s')"%(cemail_id,cpassword)
        mycursor.execute(insert)
        db.commit()
##        print"<script>location.href='login_store.py'?email_id='%s';</script>"%(cemail_id)
        print"<script language=javascript>location.href='login_store.py';</script>"
