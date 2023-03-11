n = input()
count = 0

for h in range(int(n)+1):
    for m in range(60):
        for s in range(60):
            if n in str(h) + str(m) + str(s):
                count += 1
print(count)

# in 연산자를 잘 사용하면 되는 문제!!
# 파이썬은 in, not in 연산자를 사용하며, 문자열, 리스트, 튜플, 딕셔너리에 사용 가능하다.
