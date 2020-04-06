x=int(input("enter the 1st no."))
y=int(input("enter the 2nd no."))
print("choice menu")
print("write a for addition")
print("write s for subtraction")
print("write d for division")
print("write m for multiplication")
choice=input("enter your choice:")
if choice ==str("a"):
    add=x+y
    print("the sum is",add)
elif choice==str("s"):
    sub=x-y
    print("the difference is",sub)
elif choice==str("d"):
    div=x/y
    print ("the quotient is",div)
elif choice==str("m"):
    product=x*y
    print("the product is",product)
else:
    print("your choice is incorrect!")

