import sys
import math

N = int(sys.stdin.readline())

# 상근 숫자 입력
nums = list(map(int, sys.stdin.readline().split()))

# 무제한 값 선언
ans = math.inf

ans_left = 0 
ans_right = 0

for i in range(N-1):
    # 하나씩 꺼내서 비교한다.
    current = nums[i]
 
    start = i + 1
    end = N - 1

    # 끝까지 탐색했을 때 종료
    while start <= end:
        
        mid = (start + end) // 2

        # tmp = 현재 비교 값 + 중간 값
        tmp = current + nums[mid]

        # 비교값 + 중간 값의 절대값이 이전 값보다 작다면 -> 더 최솟값을 찾았다면
        if abs(tmp) < ans:
            # 최솟값 교체
            ans = abs(tmp)
            ans_left = i
            ans_right = mid

            # tmp가 0이면 바로 정답 출력
            if tmp == 0:
                break
        
        # 만약 tmp가 음수라면  -> 
        if tmp < 0:
            # 시작을 오른쪽으로
            start = mid + 1
        
        # 양수라면 왼쪽으로
        else:
            end = mid - 1

print(nums[ans_left], nums[ans_right])

    


