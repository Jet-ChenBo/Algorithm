# 输入连续的数字(0-9)，如果有三个或以上是连续的(正序)，就简写。例如输入 12356 输出 1-356

def test(s):
    mid = []
    i = 0
    while i<len(s):
        if not mid:
            mid.append(s[i])
        else:
            if int(s[i]) - int(mid[-1]) == 1:
                mid.append(s[i])
            else:
                if len(mid) >= 3:
                    print(mid[0] + '-' +mid[-1],end='')               
                else:
                    print(''.join(mid),end='')
                mid.clear()
                i-=1
        i+=1
    if mid:
        if len(mid) >=3:
            print(mid[0] + '-' +mid[-1],end='')
        else:
            print(''.join(mid),end='')

if __name__ == '__main__':
    s = input("输入连续的数字(0-9)：")
    test(s)
