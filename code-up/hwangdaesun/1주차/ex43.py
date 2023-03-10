a,b = input().split()
a = float(a)
b = float(b)
print(format(a/b,".3f"))

# 실수의 유효숫자를 고려하여서 출력할 때, format()함수를 이용할 수도 있지만, 아래와 같은 방식을 이용하는 게 일관성있음
# print('%.3f'%c) -> 왼쪽에는 .3f와 같이 나타내고, 오른쪽에는 %변수를 사용할 것

