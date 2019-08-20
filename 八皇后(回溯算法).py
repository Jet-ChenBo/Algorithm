#八皇后算法  典型的回溯算法
#在8*8的表格里,摆放八个皇后,使任意两个皇后都不能处于同一行,同一列或同一斜线上(45)

#递归搜索解空间，寻找第n个皇后的位置
def findQueens(n):
    if n == num:
        printOut()
        return       #打印后返回到上一行的for循环
    else:
        for i in range(num):
            array[n] = i
            if check(n):
                findQueens(n + 1)

#判断是否满足约束条件
def check(n):    #用当前的皇后和前面的所有皇后比较位置
    for i in range(n):
        if array[i] == array[n]:  #不在同一列
            return False
        if abs(array[i] - array[n]) == (n - i):  #不在对角线上
            return False
    return True

#打印出每种方法
def printOut():
    global count
    count += 1
    if count > 5:   #这里为了节约时间只打印五次结果
        return
    print('the %d result'% count)
    
    for i in range(num):
        result[i][array[i]] = 1   #把皇后放到棋盘上

    for i in range(num):
        for j in range(num):
            print(result[i][j],end='  ')
            result[i][j] = 0     #打印后清0
        print()
               

if __name__ == '__main__':
    count = 0
    num = 8
    array = [0 for _ in range(num)]
    result = [[0 for _ in range(num)] for i in range(num)] 
    findQueens(0)
    print('the total result is %d'% count)


