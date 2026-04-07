import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0

    K = int(input_data[idx])
    idx += 1

    val = {}
    for _ in range(K):
        char = input_data[idx]
        idx += 1
        value = int(input_data[idx])
        idx += 1
        val[char] = value

    A = input_data[idx]
    idx += 1
    B = input_data[idx]
    
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + val.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    
    print(dp[n][m])
    print(''.join(result))

if __name__=="__main__":
    solve()
