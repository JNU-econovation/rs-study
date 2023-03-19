
# arr -> s_nums, target -> compare_num[i]
def binary_search(arr, target, start, end):
    
    # 숫자를 찾지 못했을 때
    if start > end:
        return None    
    
    mid = (start + end) // 2
    
    # 찾은 경우에 중간값 반환
    if arr[mid] == target:
        return mid
    
    # 중간값보다 target이 작으면 중간값 왼쪽 확인
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    
    # 중간값보다 target이 작으면 중간값 왼쪽 확인
    else:
        return binary_search(arr, target, mid + 1, end)


N = int(input())

# 상근 숫자 입력
s_nums = list(map(int, input().split()))
s_nums.sort()

M = int(input())

compare_nums = list(map(int, input().split()))

# 각 수가 적힌 숫자 카드를 상근이가 가지고 있는지에 대한 답 리스트
ans_list = []

for i in range(M):
    ans = binary_search(s_nums, compare_nums[i], 0, N-1)
    if ans != None:
        ans_list.append(1)
    else:
        ans_list.append(0)

# list 앞에 *를 붙이면 리스트 요소들을 한번에 출력할 수 있다고 합니다.
print(*ans_list)
