
def tree_print(a):
    length = len(a)
    layers = 0
    had_put = 0
    #计算层数
    while(length>=2**layers):
        length -=layers
        layers += 1
    #计算每层节点数,最后一层不计算
    for i in range(0,layers-1):
        index = 2**i
        mid = []
        for j in range(0+had_put,index+had_put):
            mid.append(a[j])
        had_put += index
        mid.sort()
        list_print(mid)
        print()
    #计算最后一层
    mid = []
    for i in range(had_put,len(a)):
        mid.append(a[i])
    mid.sort()
    list_print(mid)
    print()

# 不换行输出list
def list_print(a):
    for i in a:
        print(i,end=" ")

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
    lines = case_num*2 + 1
    for i in range(0,len(items)):
        if i == 0:
            pass
        elif i%2 == 0:
            tree_print(items[i])
        else:
            pass

        lines -= 1
        if lines == 0:
            break

except:
    pass

# if __name__ == '__main__':
#     a = [7,5,6,2,3,1]
#     tree_print(a)