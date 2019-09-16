# 一元可以买一瓶水,m个瓶子可以换一元,那么n元最多能喝到几瓶水
def func(n,m):
    count = 0
    while n>m-1:
        count += n//m*m   # 每次买m的倍数瓶
        n = n//m + n%m    # 瓶子换的钱加上没用的钱
    count += n            # 最后还剩n<m元钱
    print(count)


if __name__ == '__main__':
    n = eval(input())  # 多少钱
    m = eval(input())  # 几个瓶子换一瓶
    func(n,m)
