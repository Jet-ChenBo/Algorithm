# n个人围成一圈,顺序排号,从第一个开始报数(1到3),数到3的出局,问最后一个人的编号


n = int(input("一共多少人："))

num = []
for i in range(n):
    num.append(i + 1)

m = 0 # 出局的人数
i = 0 # 报数的人
k = 0 # 该报的数

while m < n-1:
    if num[i] != 0:
        k += 1
    if k == 3:
        num[i] = 0
        k = 0
        m += 1
    i += 1
    if i == n:
        i = 0

i = 0
while num[i] == 0:
    i += 1
print(num[i])
