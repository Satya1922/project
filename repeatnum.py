num = int(input())
st = list(map(int,input().split()))
st.sort()
a = []
for i in range(len(st)-1):
    if st[i]==st[i+1]:
        a.append(st[i])
if a:
    for x in  set(a):
        print(x,end=" ")
else:
    print("unique")
