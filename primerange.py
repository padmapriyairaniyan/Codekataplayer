n=int(input())
n1=int(input())
l=0
c=0;

for k in range(n,n1):
    if(k==1):
        pass
    else:
        f=0;
        for i in range(2,k):
            if(k%i==0):
                f=1;
                break;

        if(f==0):
            l=l+1
print(l)
