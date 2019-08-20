#将一个正整数分解质因数，例如输入90，输出 90=2*3*3*5

def reduceNum(n):
    if not isinstance(n, int) or n < 1:
        print("请输入大于0的整数")
        return
    elif n == 1:
        print("1=1")
        return
    else:
        print("\n{}=".format(n),end='')
        while(n != 1):
            for i in range(2, n+1):
                if n % i == 0:
                    n = n // i
                    if n == 1:
                        print('{}'.format(i),end ='')
                        break
                    else:
                        print('{}*'.format(i),end ='')
                        break
            
for i in range(20):
    reduceNum(i)
