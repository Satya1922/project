num=int(input())
result=0
while ((num!=0) and (num<=1000000000000000000)) :
    r=num%10
    result+=pow(r,2)
    num//=10
print(result)
