n = int(input())
list_s = input().split()
list = list(map(int, list_s))

for i in range(1,24):
    print(list.count(i), end=" ")

# map() 함수 : map(function, iterable)
# 첫 번째 매개변수로는 함수가 오고, 두 번째 매개변수로는 반복 가능한 자료형(리스트,튜플 등)이 온다.
# map() 함수의 반환값은 map 객체이다.
# 함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 
# 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 방식이다.
