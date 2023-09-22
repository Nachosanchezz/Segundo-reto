from math import cell  

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    d = abs(a-b)
    print(cell(d/(c*2)))     #Cell es redondear hacia arriba