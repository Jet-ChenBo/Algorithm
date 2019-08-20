#求一个序列的最大子序列(连续的数字最大和)
#复杂度为n
#注意两个列表赋值，相当于给列表增加一个引用

def Max(m):
    
    maxMidList = []  #存放当前最大子序列
    maxMidValue = 0  #记录当前最大子序列和
    maxList = []     #存放最终的最大子序列
    maxValue = 0     #存放最终的最大子序列和

    for i in m:     
        maxMidValue += i
        maxMidList.append(i)
        
        if maxMidValue > maxValue:
            maxValue = maxMidValue
    #maxList = maxMidList 错误，这只是增加了maxMidList的引用，结果为maxMidList
            maxList = maxMidList.copy()
        elif maxMidValue <= 0:
            maxMidList.clear()
            maxMidValue = 0
            
    maxList.append(maxValue)
    return maxList
   
    
def main():
    a = [2,5,-8,7,4,-3,-2,9,-4,7,6,-3,-2,-1,-6]
    b = Max(a)
    print("最大子序列是：{}".format(b[:-1]))
    print("和为%2d" % b[-1])

if __name__ == '__main__':
    main()
    
