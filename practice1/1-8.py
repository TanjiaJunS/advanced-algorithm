
def math_print(a):
    A = a[0]
    B = a[1]
    C = a[2]
    sum = power(A,B)
    print(sum%C)

# 递归实现
def power(x, y):
    if (y == 0):
        return 1
    elif (int(y % 2) == 0):
        return (power(x, int(y / 2)) * power(x, int(y / 2)))
    else:
        return (x * power(x, int(y / 2)) * power(x, int(y / 2)))

#获取输入的函数

import sys
try:
    items = []
    while True:
        item = sys.stdin.readline().strip()
        if item == '':
            break
        item = list(map(int,list(item.split())))
        items.append(item)
    #print(items)
    case_num = items[0][0]
    for i in items:
        if len(i) == 1:
            continue
        else:
            math_print(i)

except:
    pass