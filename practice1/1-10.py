# 此题可以想象成把数据按顺序装入桶中，m即是给定的桶数，问桶的容量至少应该为多少才能恰好把这些数装入k个桶中（按顺序装的）。
# 首先我们可以知道，桶的容量最少不会小于数组中的最大值，即桶容量的最小值为数组中的最大值（最大书页数量）（小于的话，这个数没法装进任何桶中），
# 假设只需要一个桶，那么其容量应该是数组所有元素的和，即桶容量的最大值；其次，桶数量越多，需要的桶的容量就可以越少，
# 在给定的桶数量m的时候，找最小的桶容量，就可以把所有的数依次装入k个桶中。
# 如果需要的桶数量大于给定的桶数量k，说明桶容量太小了，只需要增加桶的容量，计算当前容量所需要的桶数，当其刚好等于给定的桶数m时，
# 此时的桶容量，且有m个数量时，刚好可以装下所有的数。此时再计算每个桶中数之和最大的数，则为最后的输出结果
# 假设有数值：以 m = 5 为例，最小桶容量则为13，此时每个桶中的值为 12 13 10 8 9 ，则最大页数为13，即为所求的值，
# 不必考虑，这一定是所有排列中最小的值，因为再小的话，就需要增加桶的数量。
# 6,1,2,3,8,5,2,3,5,8,9
# 桶容量设置为     ：9  10 11 12 13 14 15 16 17 ...sum
# 对应需要桶数量为  ：7  7  6  6  5  5  5  4  4 ...  1


# 计算给定的数列表和桶的数量时，所需要的最小值
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
    book_num = []
    books = []
    student = []
    for i in range(0, len(items)):
        if i == 0:
            pass
        else:
            if i % 3 == 1:
                book_num.append(items[i])
            if i % 3 == 2:
                books.append(items[i])
            if i % 3 == 0:
                student.append(items[i])
    for i in range(0, case_num):
        if book_num[i][0] < student[i][0]:
            print(-1)
        elif book_num[i][0] == student[i][0]:
            print(max(books[i]))
        else:
            print(arrange(books[i], student[i][0]))
    # print(book_num,books,student)

except:
    pass

# if __name__ == '__main__':
#     a = [6,1,2,3,8,5,2,3,5,8,9]
#     mimi = 9
#     min_a = 3
#     an,ab =get_num_bucket(a,mimi)
#     m = arrange(a,min_a)
#     print(an)
#     print(ab)
#     print(m)
