number = 10
print number

floatNumber = 10.007
print floatNumber

name='surajit'
print name

a = b = c = 5
print a,b,c

first,second,third = 5,6.003 ,'surajit'
print first,second,third

demoTuple =('surajit','23')
print demoTuple,demoTuple[0],demoTuple[1]
# print demoTuple[3]

myObject = {'name':'surajit','title':'chongder','age':23,'dob':1994}
print myObject
print myObject.keys()
print myObject.values()

# print myObject[name]

myString = '''welcome
to
thoughtworks'''
print myString

if (10 is not 10):
    print 'iam here'
else :
    print'oooola'

if (10 is 10):
    print 'iam here'
else :
    print'oooola'

a=3
if a==10:
    print  "i am heralal"
elif a==3:
    print "i am chunnu"
else:
    print "panna"

b=5
for b in range(0,4):
    print b+1

for c in [4,5,6,7]:
    if c==6:
        print"aa yaaa"
    print c


stringDemo = "relex"
print (stringDemo[0]==stringDemo[-5])

arrayDemo = [1,2,4,5]
print (arrayDemo[0]==arrayDemo[-4])

string1="    Hello Python";
print string1.lstrip();
