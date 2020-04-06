#Enter a two nos. 'n' and 'k' and cheak whether 'n' is divisible by 'k' or not.
n=int(input("Enter a no.(n):"))
k=int(input("Enter a no.(k):"))
if n%k==0:
    print(n,"is divisible by",k)
else:
    print(n,"is not divisible by",k)
