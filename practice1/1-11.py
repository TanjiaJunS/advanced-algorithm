if __name__ == '__main__':
    for _ in range(int(input())):
        num = list(map(int, input().split(' ')))[0]
        i = 1
        nums_list = []
        while i <= num:
            num_list = list(map(int, input().split(' ')))
            num_list[1] = 1000 - num_list[1]
            nums_list.append(num_list)
            i += 1
        nums_list.sort()
        for sorted_list in nums_list:
            sorted_list[1] = 1000 - sorted_list[1]
        for score_list in nums_list:
            score_str = []
            for score_index in range(len(score_list)):
                if score_index == len(score_list) - 1:
                    score_str.append(str(score_list[score_index]))
                else:
                    score_str.append('{0} '.format(score_list[score_index]))
            print(''.join(score_str))