n, x = map(int, input().split())

report = []

for _ in range(x):
    report.append(map(float, input(.split())))
    
for i in zip(*report):
    print(sum(i) / len(i))
    