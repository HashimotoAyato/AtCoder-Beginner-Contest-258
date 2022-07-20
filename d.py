from binascii import b2a_hex
import numpy as np

N, X = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = np.zeros(N+1, int)

for i in range(N):
    dp[i+1] = dp[i] + A[i] + B[i]

times = []
for i in range(N):
    times.append(dp[i]+A[i]+B[i]*(X-i))

print(min(times))
