# 采取逐渐缩小的步长，对同一个步长下的数进行插入排序

def shell_Sort(li):
    length = len(li)
    # 步长 
    gap = length//2
    while gap > 0:
        # 对同一个步长下的数进行插入排序
        for i in range(gap, length):
            j = i
            while j > 0:
                if li[j] < li[j-gap]:
                    li[j],li[j-gap] = li[j-gap],li[j]
                    j -= gap
                else:
                    break
        # 缩短步长
        gap //= 2


li = [8,5,2,7,1,3,6,4]
shell_Sort(li)
print(li)
