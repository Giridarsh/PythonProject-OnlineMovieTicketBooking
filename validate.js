function isnumber(evt,t)
{
num=window.document.reg.pincode.value;
kcode=evt.which;
//alert(kcode);
if(kcode>47&&kcode<=57)
{
return true;
}
else
{
alert("enter  numbers only");
return false;
}
}

function emailcheck()
{
mail=window.document.reg.em.value;
//alert(mail);
dotpos=mail.lastIndexOf(".");
atpos=mail.indexOf("@");
//alert(dotpos);
//alert(atpos);
diff=dotpos-atpos;
//alert(diff);
if(diff<=4)
{
alert("enter valid email-id");

return false;
document.reg.em.focus();
}
else{
	return true;
}
}
function checkno(ev,th)
{
no=window.document.reg.pincode.value;
kcode=ev.which;
//alert(kcode);
if(kcode>47&&kcode<=57)
{
return true;
}
else
{
alert("enter  numbers only");
return false;
}										
}
function cstate()
{
if(country!="0")
{
window.document.reg.state.disabled=false;
}
}
function ccity()
{
if(state!="0")
{
window.document.reg.city.disabled=false;
}
}
function valid()
{
name=document.reg.fname.value;
con=document.reg.country.value;
state=document.reg.state.value;
city=document.reg.city.value;
pcode=document.reg.pincode.value;
code=pcode.length;
mail=document.reg.em.value;
phno=document.reg.number.value;
num=phno.length;
gen=document.reg.gender.value;
addr=document.reg.addr.value;
if(name=="")
{
alert("enter the namefield");
document.reg.fname.focus();
return false;
}
else if(con=="0")
{
alert("select country");
document.reg.country.focus();
return false;
}
else if(state=="0")
{
alert("select state");
document.reg.state.focus();
return false;
}
else if(city=="0")
{
alert("select city");
document.reg.city.focus();
return false;
}
else if(pcode=="")
{
alert("enter Pincode");
document.reg.pincode.focus();
return false;
}	
else if(code<6)
{
alert("enter valid-pincode");
document.reg.pincode.focus();
return false;
}
else if(mail=="")
{
alert("enter email-id");
return false;

}
else if(phno=="")
{
alert("enter ph.no");
document.reg.number.focus();
return false;
}
else if(num<10)
{
alert("enter valid-ph.no");
document.reg.number.focus();
return false;
}
else if(gen=="")
{
alert("select gender");
return false;document.reg.em.focus();
}
else if(addr=="")
{
alert("enter address");
document.reg.addr.focus();
return false;
}
else{}
	
}

function emailcheck()
{
mail=window.document.login.em.value;
//alert(mail);
dotpos=mail.lastIndexOf(".");
atpos=mail.indexOf("@");
//alert(dotpos);
//alert(atpos);
diff=dotpos-atpos;
//alert(diff);
if(diff<4)
{
alert("enter valid email-id");
return false;
}
else
{
 return true;
}
}

function clogin()
{
em=document.login.em.value;
pwd=document.login.pwd.value;
if(em=="")
{
	alert("enter empty email-id fields")
	//document.login.em.focus();
	return false;
	
	
	
}
else if(pwd=="")
{
	alert("enter empty password fields")
	document.login.pwd.focus();
	return false;
	
	
	
}
else
{
}
}
function editbbutton()
{
	alert("hii")
	window.location.href="home.py";

}