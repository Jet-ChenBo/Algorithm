# 一元可以买一瓶水,两个瓶子可以换一元,那么n元最多能喝到几瓶水
def func(n):
    count = 0
    while n>1:
        count += n//2*2   # 每次买偶数瓶
        n = n//2 + n%2    # 瓶子换的钱加上没用的钱
    count += 1            # 最后还剩一元钱
    print(count)


if __name__ == '__main__':
    n = eval(input())
    func(n)
