import math
print("The expression is in the form: ax^2 + bx + c")
a = int(input("Enter te value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
d = (b*b)-(4*a*c)
if d>0:
    temp=math.sqrt(d)
    x1= (((-1)*b)-temp)/(2*a)
    x2= (((-1)*b)+temp)/(2*a)
    print("The roots are",x1,"and",x2)
elif d==0:
    x= ((-1)*b)/(2*a)
    print("The equal roots are",x ,"and",x)
else:
    print("Real roots does not exist")
