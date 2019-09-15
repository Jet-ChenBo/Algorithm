def func(lst):
    length = len(lst)  # 数组长度
    if length<3:
        return False
    max_num = max(lst)  # 数组最大值
    min_num = min(lst)  # 数组最小值  
    tol = (max_num - min_num) / (length-1)  # 公差
    if tol == 0:
        return True
    # 判断数组里每个数能否从最小值开始加上n个公差得到
    for i in lst:
        sub = i - min_num
        if sub/tol != sub // tol:
            return False
    return True


print(func([1,1,1,1,1]))
