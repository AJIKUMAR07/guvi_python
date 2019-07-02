get=int(input())
temp=get
palin=0
while get!=0:
         digit=get%10
         palin=palin*10+digit
         get=get//10
if temp==palin:
    print("yes")
else:
    print("no")
