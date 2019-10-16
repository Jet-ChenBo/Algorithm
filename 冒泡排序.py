# 两两比较，后者大于前者就交换位置，每一轮会把最大的依次排在列表右边
# 时间复杂度：O(n2)

import timeit

def bubbleSort(li):
    for i in range(len(li)-1, 0 ,-1):
        # 设置flag，如果有一轮一次都没交换，说明已经排好序
        flag = True
        for j in range(i):
            if li[j]>li[j+1]:
                flag = False
                li[j],li[j+1] = li[j+1],li[j]
        if flag:
            break
    return li


li = [8,7,6,5,1,2,3,4]
print(bubbleSort(li))
# 测试运行排序代码10000次所需时间，可以发现加了flag比没加快的多
print(timeit.timeit(stmt='bubbleSort(li)',setup='from __main__ import bubbleSort,li', number=10000))
    
