side_a=int(input("Enter the first side(a):"))
side_b=int(input("Enter the second side(b):"))
side_c=int(input("Enter the third side(c):"))
if side_a==side_b and side_a==side_c:
    print("The triangle is an equilateral triangle.")
elif side_a==side_b or side_a==side_c or side_b==side_c:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is scalene triangle.")