N, Q = map(int, input().split())
S = list(input())

sum = 0
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        sum = (sum + x) % N
    if t == 2:
        print(S[(N-sum+x-1)%N])      