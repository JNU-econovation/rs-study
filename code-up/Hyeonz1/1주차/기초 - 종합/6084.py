# 내용 : 필요한 저장 공간 구해서, 소숫점 첫째 자리까지의 정확도로 출력
    # 특정 소숫점 자리까지의 실수값을 구해야 함.
h, b, c, s = map(int, input().split())

result = h * b * c * s / 8 / 1024 / 1024

print(round(result, 1), "MB")

