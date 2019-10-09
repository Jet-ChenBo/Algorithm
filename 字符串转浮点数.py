# 将一个字符串转换成小数，不用内置的函数
def str_to_float(s):
    num = 0
    flag = 1  # 是否是整数部分
    c = 1 # 小数的位数
    for i in s:
        if not (i.isdigit() or i=='.'):
            return '该字符串不能转化为浮点数'
        elif i == '.':
            flag = 0
        else:
            if flag:
                num = num*10 + int(i)
            else:
                num += int(i)/(10**c)
                c += 1
    return num

print(str_to_float('189.1213'))
