# 以列表第一个值为中间值，将列表分割成左右两部分,然后对左右两部分做同样的操作
# 最优时间复杂度：nlogn 每次分割结果都是左右一样多
# 最坏时间复杂度：n2    每次只能分成一部分(左或右)

def quick_Sort(li):
    if len(li) < 2:
        return li
    length = len(li)
    mid_value = li[0]
    low = 0
    high = length-1
    while low < high:
        # high左移
        while low < high and li[high] > mid_value:
            high -= 1
        li[low] = li[high]

        # low右移
        while low < high and li[low] <= mid_value:
            low += 1
        li[high] = li[low]
    # 填充中间值
    li[low] = mid_value
    # 将左右两部分再次排序
    return quick_Sort(li[0:low]) + [li[low]] + quick_Sort(li[low+1:])



li = [5,1,7,1,7,5,3,8,6,13,2,4,12]
print(quick_Sort(li))
