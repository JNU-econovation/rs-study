# 용액
import copy
import sys
sys.setrecursionlimit(10**7)


# 입력
total_liquid = int(input())
liquids = list(map(int, input().split()))
sum_list = []
index_list = []

# 이진 탐색 함수 구현
# -98을 넘겨받으면, 내가 찾고싶은 수는 -98을 더했을 때, 절댓값이 가장 작은 값이 나오는 수 : 용액 중에 98에 가장 가까운 수
def binary_search(array, target, start, end):

    mid = (start + end) // 2

    if start == end:
         if abs(array[mid] - target) > abs(array[mid - 1] - target):
              return array.index(array[mid - 1]) # 찾고자 하는 값에 가장 가까운 수와 그 수의 인덱스를 return 
         else:
              return array.index(array[mid])

    if array[mid] == target:
         return array.index(array[mid])

    elif array[mid] > target:
         return binary_search(array, target, start, mid)

    else:
         return binary_search(array, target, mid + 1, end)


for liquid in range(total_liquid):
     target1_index = liquid # bfs 적용한 용액의 인덱스
     target2_index = binary_search(liquids, -liquids[liquid], 0, total_liquid - 1) # bfs 결과 인덱스
     sum = liquids[target1_index] + liquids[target2_index] # 용액합을 저장한 index
     
     sum_list.append(sum) # 합들을 저장한 배열 만들기
     index_list.append(target2_index) # bfs 결과 인덱스를 저장한 배열 


# 0에 가장 가까운 용액을 어떻게 찾지?
sorted_list = copy.deepcopy(sum_list)
sorted_list.sort()
zero = sorted_list[binary_search(sorted_list, 0, 0, total_liquid - 1)]
sum_list_index = sum_list.index(zero)


# 출력 
# sum이 0에 가장 가까운 두 용액을 출력
print(liquids[sum_list_index], liquids[index_list[sum_list_index]], sep = ' ')



