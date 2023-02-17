a,b,c=int(input().split())
list=[a,b,c]
for i in list:
    if i%2==0:
        print("짝")
    else:
        print("홀")