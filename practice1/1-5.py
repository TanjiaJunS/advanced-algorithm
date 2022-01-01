#和1-10类似，修改一下数据分割方式，以及比较工人与木板的数量判断输出（函数的备注请忽略）

def arrange(a, m):
    # min_page = 0
    max_page = 0  # 最大页数
    capacity_min = max(a)  # 桶的最小容量
    capacity_max = 0
    for i in a:
        capacity_max += i
    # 增加桶容量，计算每一容量的桶全部装下这些数据，所需要的数量（随着容量增加，桶的数量会减少）。当桶的数量和给定的数量m相等时停止
    for i in range(capacity_min, capacity_max):
        bucket_num, cap_list = get_num_bucket(a, i)
        if bucket_num == m:
            # min_page = min(cap_list)
            max_page = max(cap_list)
            break
    return max_page


# 传入数列表，和桶容量，返回所需要的桶的数量, 以及每桶装了多少
def get_num_bucket(a, capacity_min):
    # 桶
    cap = []
    # 桶数量
    bucket_num = 0
    # 每个桶装的数值和
    trem = 0
    # 将数据从头到尾，逐个放入桶中，当桶放不下时，用下一个桶，直到剩下最后一个桶
    for i in range(0, len(a)):
        if i + 1 < len(a):
            trem = trem + a[i]
            if trem + a[i + 1] > capacity_min:
                bucket_num = bucket_num + 1
                cap.append(trem)
                trem = 0
    # 计算剩余数量，再放入最后一个桶，这一步是因为在上一步循环中，因为if语句的判断，无法计算最后剩余的数值（剩余的数值之和肯定小于桶容量），
    # 所以多出一步计算
    en = 0 #所有数据之和
    le = 0 #桶中已装入数据之和
    for i in a:
        en = en + i
    for i in cap:
        le = le + i
    cap.append(en - le)
    return bucket_num + 1, cap #返回 桶数量 和 桶内数据和的列表


# 获取输入的函数

import sys

try:
    items = []
    while True:
        item = sys.stdin.readline().strip()
        if item == '':
            break
        item = list(map(int, list(item.split())))
        items.append(item)
    # print(items)
    case_num = items[0][0]
    painter_boardNum  = []
    boards = []
    for i in range(0, len(items)):
        if i == 0:
            pass
        else:
            if i % 2 == 1:
                painter_boardNum.append(items[i])
            if i % 2 == 0:
                boards.append(items[i])
    for i in range(0, case_num):
        if painter_boardNum[i][0] >= painter_boardNum[i][1]:
            print(max(boards[i]))
        else:
            print(arrange(boards[i],painter_boardNum[i][0]))
    # print(book_num,books,student)

except:
    pass