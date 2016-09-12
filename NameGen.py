#Python Google Acct Gen
import random as r
a="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
b=list(a)
c="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
d=list(c)
e="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+{}~"
f=list(c)

#Testname
rrr=r.randint(7,20)
testName=""
for j in range(rrr):
	testName+=c[r.randint(0,len(c)-1)]
firstName=testName

rrr=r.randint(7,20)
testName=""
for j in range(rrr):
	testName+=c[r.randint(0,len(c)-1)]
lastName=testName

rrr=r.randint(5,10)
testName=""
for j in range(rrr):
	testName+=f[r.randint(0,len(f)-1)]
userName=testName

rrr=r.randint(15,40)
testName=""
for j in range(rrr):
	testName+=b[r.randint(0,len(b)-1)]
passWord=testName

#Assign Month
month = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
day = r.randint(1,28)
year = int("19"+str(r.randint(0,8))+str(r.randint(0,9)))
monthI = r.randint(0,len(month))

gender=""
gen=r.randint(0,3)
if(gen==1):
	gender="Female"
else:
	gender="Male"
print("First Name: {}\nLast Name: {}\nUsername: {}\nDate of Birth: {}\nPassword: {}\nGender: {}".format(firstName,lastName,userName,(month[monthI],day,year),passWord,gender))
#print("{}:{}:{}".format(month[monthI],day,year))
genFile=open("Output","w+")
genFile.write("First Name: {}\nLast Name: {}\nUsername: {}\nDate of Birth: {}\nPassword: {}\nGender: {}".format(firstName,lastName,userName,(month[monthI],day,year),passWord,gender))
genFile.close()