n, m, k = map(int, input().split())
arr = list(map(int, input().split()))


arr.sort(reverse=True)


if (m == k):

    print(arr[0] * k)

else:
    
    quo = m // (k + 1)
    rem = m % (k + 1)

    result = quo * k * arr[0] + quo * arr[1] + rem * k

    print(result)