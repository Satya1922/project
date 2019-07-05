a,b=map(int,(input().split()))
s=0
for x in range(2,b):
        if(a%x==0 and b%x==0):
            s=x
print(s)

