a,b = input().split()
a = int(a)
b = int(b)
a = bool(a)
b = bool(b)
print((not a and b) or (a and not b))

# 논리연산 XOR구현
# 1을 입력할 때는 False가 나오지만, 0을 입력할 때는 숫자 0이 출력된다.

# 파이썬은 참 거짓을 위해 반드시 bool 객체, 즉 True,False의 형태로만 취급하지 않는다.
# False는 숫자 0, 비어있는 문자열 등 그 객체 자체이다.

# 파이썬의 and 연산
# A and B에서 A가 거짓을 뜻하는 객체라면 B는 연산을 하지 않고 바로 거짓을 반환합니다.
# 이때 False를 반환하지 않고 A가 이미 거짓을 뜻하는 객체이기때문에 그대로 A를 반환합니다.

# or 연산도 마찬가지!

# 파이썬의 not 연산
# 반환값은 True, False

# 확실히 하기위해 bool()함수를 활용하는 건 어떨까??
