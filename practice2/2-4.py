def distribute(per, current_time, distribute_path):
    global n, time, res, task_list, distribute_tag
    if per == n:
        if current_time < time:
            time = current_time
            res = distribute_path.copy()
        return

    # 遍历任务
    for i in range(n):
        if distribute_tag[i] == 1:
            continue
        # 分配
        distribute_tag[i] = 1
        distribute_path.append(i+1)
        current_time += task_list[per][i]
        distribute(per+1, current_time, distribute_path)
        # 回溯
        distribute_tag[i] = 0
        current_time -= task_list[per][i]
        distribute_path.remove(i+1)


for _ in range(int(input())):
    n = int(input())
    input_list = list(map(str, input().split(',')))
    input_list.sort()
    task_list = [[] * n for row in range(n)]
    for key in input_list:
        key_list = key.split(' ')
        task_list[int(key_list[0]) - 1].append(int(key_list[2]))
    time = 999999
    distribute_tag = [0] * n
    res = []
    distribute(0, 0, [])
    print_str = []
    for key in res:
        print_str.append('{0} '.format(key))
    result = ''.join(print_str)
    print(result[:-1])