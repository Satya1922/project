ch=int(input())
if(ch%4==0 and ch%100!=0 or ch%400==0):
    print("yes")
else:
    print("no")
