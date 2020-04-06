purchase_amt=int(input("Enter the purchase amount(in Rs.):"))
if purchase_amt<=400:
    discount=0
elif purchase_amt<=5000 and purchase_amt>400:
    discount=400
elif purchase_amt>5000 and purchase_amt<=10000:
    discount=800
elif purchase_amt>10000 and purchase_amt<=20000:
    discount=1000
else:
    discount=2000
    amt_after_discount=(purchase_amt-discount)
    additional_discount=(3/100)*amt_after_discount
    discount=discount+additional_discount
net_amt=purchase_amt-discount

print("The discount is Rs.",discount,"and the net amount after discount is Rs.",net_amt)