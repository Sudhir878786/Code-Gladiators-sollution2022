t = int(input())
for i in range(t):
    n = int(input())
    g = int(input())
    prices = list(map(int, input().split()))
    prices.sort()
    print(sum(prices[:n]))