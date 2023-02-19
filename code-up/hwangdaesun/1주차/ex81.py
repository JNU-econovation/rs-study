a = input()
n = int(a,16)
for i in range(1,16):
    print("%X"%n,"*%X"%i,"=%X"%(n*i),sep="")

# int(a,16)이 '16진수인 a를 정수로 바꿔'라는 뜻
# %(n*i)를 하지 않고,%n*i를 함 -> 문자열이 곱해짐... 


