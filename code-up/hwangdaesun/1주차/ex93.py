n = int(input())
list_s = input().split()

list = list(map(int, list_s))
list.reverse()

print(reversed(list))

for i in list:
    print(i, end=" ")

# list.reverse()는 반환값이 None이므로 for i in list.reverse()는 불가능하다.
