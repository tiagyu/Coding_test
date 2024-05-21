#구간 합 구하기1(백준 11659번)

N,M = map(int,input().split())
numbers = list(map(int,input().split()))

sum = 0
sum_list = [0]

for s in numbers:
    sum = sum + s
    sum_list.append(sum)
    print(sum_list)

for s in range(M):
    i, j = map(int,input().split())
    print(sum_list[j]-sum_list[i-1])

#코드 구현(책)
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
sum_list = [0]
sum = 0

for i in numbers:
    sum = sum + i
    sum_list.append(sum)
    
for i in range(M):
    s, e = map(int,input().split())
    print(sum_list[e]-sum_list[s-1])