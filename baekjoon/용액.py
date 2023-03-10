import sys

n = int(input())
drink = list(map(int,sys.stdin.readline().strip().split()))

def search(array,target,start,end):
    while(1):
        mid = (start + end) // 2
        sum = array[mid] + target
        if(end - start <= 1):
            endSum = abs(array[end] + target)
            startSum = abs(array[start] + target)
            if(endSum > startSum):
                return start, startSum
            else:
                return end, endSum
        if(sum < 0):
            start = mid
        elif(sum > 0):
            end = mid
        else:
            print(target,array[mid],end=" ")
            sys.exit()

answerList = []
answerIndexes = []
# 0부터 n-2까지 n=4 0,1,2
for i in range(n-1):
    answerIndex, answer = search(drink,drink[i],i+1,n-1)
    answerList.append(answer)
    answerIndexes.append((i,answerIndex))

a = answerList.index(min(answerList))
index = answerIndexes.pop(a)
print(drink[index[0]],drink[index[1]],end=" ")



    

