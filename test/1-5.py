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
    max = items[0][0]
    for i in range(1,max+1):
        item = items[i]
        sum = 0
        for i in item:
            sum = sum + i
        print(sum - item[0])
except:
    pass

#题目中可能会出现如下用例：
# 2
# 4 1 2 3 4
# 5 1 2 3 4 5
# 3 2 1 3