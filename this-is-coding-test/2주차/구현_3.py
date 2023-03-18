# 왕실의 나이트

#  x축은 a~h  , y 축은 1~8
arr = input()
x= ord(arr[0])-ord('a')+1
y=int(arr[1])
fcount = 0
scount = 0
def transfer(x,y,count):
   if x-2>0 and y-1>0:
       count+=1
   if x-2>0 and y+1<=8:
       count+=1
   if x+2<=8 and y-1>0:
       count+=1
   if x+2<=8 and y+1<=8:
       count+=1
   return count

fcount=transfer(x,y,fcount)
scount=transfer(y,x,scount)

print(fcount+scount)
