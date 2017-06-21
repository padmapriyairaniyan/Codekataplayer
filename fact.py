n=int(input("enter a number"))
k=1
if(n<=0):
    print("invalid input")
else:
    for i in range(1,n+1):
        k=k*i
print(k)
