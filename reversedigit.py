n=int(input("enter a number"))
n1=0
n1=int(n1)
r1=n
while n!=0:
    r=n%10
    r=int(r)
    n1=n1*10+r
    n=n//10
print("the reversed number is\t"+str(n1))
