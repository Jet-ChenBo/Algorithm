# 每一轮选择最小的放在左边
# 第一轮从0...n 中选择出最小的与0号位置交换
# 第二轮从1...n 中选择出最小的与1号位置交换
# .....

def choiceSort(li):
    length = len(li)
    for i in range(0,length-1):
        # 记录最小值
        min = li[i]
        # 记录最小值的下标
        subscript = i
        for j in range(i+1,length):
            if li[j]<min:
                min = li[j]
                subscript = j
        li[i],li[subscript] = li[subscript],li[i]
    return li


if __name__ == '__main__':
    li = [9,8,7,6,5,4,3,2,1]
    print(choiceSort(li))
