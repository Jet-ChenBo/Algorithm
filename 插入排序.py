# 从第二个元素开始(下标为1)，向前面插入

def insertSort(li):
    for i in range(1,len(li)):
        # j跟随着当前需要插入的元素
        for j in range(i,0,-1):
            # 比前面的元素小，就交换
            if li[j] < li[j-1]:
                li[j],li[j-1] = li[j-1],li[j]
            else:
                break
    return li


if __name__ == '__main__':
    li = [8,7,6,5,4,3,2,1]
    print(insertSort(li))
            
