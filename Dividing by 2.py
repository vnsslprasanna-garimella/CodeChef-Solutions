# Problem: Dividing by 2 (DIV2)
# Link: https://www.codechef.com/problems/DIV2
# Platform: CodeChef
# Language: Python 3

# cook your dish here
# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = {}
    total = {}

    for x in a:
        steps = 0
        while True:
            if x not in cnt:
                cnt[x] = 0
                total[x] = 0

            cnt[x] += 1
            total[x] += steps

            if x == 0:
                break

            x //= 2
            steps += 1

    ans = float('inf')

    for v in cnt:
        if cnt[v] == n:
            ans = min(ans, total[v])

    print(ans)