# 将重复出现的字符串后面加1、2、3等数字来区分，数组原顺序不变

def func(lst):
    new_lst = []
    for index,value in enumerate(lst):  # enumerate:同时获取数组的下标和对应的值
        if lst.count(value) == 1:      # lst.count(value):计算lst中有多个value
            new_lst.append(value)
        else:
            x = lst[:index].count(value)  # 获取这个value的前面有多个value
            new_lst.append(value+str(x+1))  # 比如有0个，那么就+1
    print(new_lst)

func(['ab','ab','cd','cd','abc','a','abc'])
            
