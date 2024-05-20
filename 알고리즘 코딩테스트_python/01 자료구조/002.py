#평균 구하기(백준 1546번)
n = int(input())
score = list(map(int,input().split()))
score.sort()
max = score[-1]

sum = 0
for i in score:
    average = (i / max) * 100
    sum += average/n

print(sum)

#코드 구현(책)
n = input()
mylist = list(map(int,input().split()))
mymax = max(mylist)
sum = sum(mylist)
print(sum*100/mymax/int(n)) #한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환해 로직을 간단하게 할 수 있음
