n=int(input())
answers = list(map(int,input().split()))
hard=False
for i in range(n):
    if answers[i]==1:
        hard=True

if hard:
    print("Hard")
else:
    print("Easy")