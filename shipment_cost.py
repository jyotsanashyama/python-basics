order_unit=int(input("Enter the order unit:"))
s_c=input("Are you a special customer?(yes/no):")#s_c=special customer
per_unit_price=0
total_cost=0
if order_unit<15:
    per_unit_price=25000
elif order_unit>=16 and order_unit<=20:
    per_unit_price=24500
elif order_unit>=21 and order_unit<=30:
    per_unit_price=24000
elif order_unit>=31 and order_unit<=50:
    per_unit_price=23500
else:
    per_unit_price=23000
total_cost=order_unit*per_unit_price

if s_c=='yes':
    discount=(10/100)*per_unit_price
else:
    discount=0
total_cost=total_cost-discount

print("The total cost is",total_cost)




