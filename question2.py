def solution(A, K):
    ans = []
    for x, y in enumerate(A):
        n = x + K
        if n >= len(A):
            n = n - len(A)
        ans.insert(n, y)
    return ans


print(solution([3,8,9,7,6], 3))
print(solution([0,0,0], 1))
print(solution([1,2,3,4], 4))