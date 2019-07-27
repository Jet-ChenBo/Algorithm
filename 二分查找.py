# 在列表首尾设置两个游标low、high
# 将待查找数字与两个游标的中间位置(mid)进行比较
# 如果带查找数字大于中间位置，那么low = mid+1，否则 high = mid-1。

def binary_find(li,item):
    low = 0
    high = len(li)-1
    while low <= high:
        mid = (low+high) // 2
        if item < li[mid]:
            high = mid - 1
            continue
        elif item > li[mid]:
            low = mid + 1
        else:
            return True
    return False


if __name__ == '__main__':
    li=[1,3,4,5,7,9,12,23,45]
    print(binary_find(li,23))
