n=int(input("Enter a number: "))
order=len(str(n))
s=0
temp=n
while temp>0:
    digit=temp%10
    s=s+digit**order
    temp//=10
if n==s:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
