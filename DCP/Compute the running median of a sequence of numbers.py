def median(lst):
    median_lst = []
    temp = []
    for i in range(len(lst)):
        temp.append(lst[i])
        temp.sort()
        if len(temp) <= 1:
            median_lst.append(temp[i])
        elif len(temp) > 1 and len(temp) % 2 == 1:
            middle_index = int(len(temp) / 2)
            middle_value = temp[middle_index]
            median_lst.append(middle_value)
        elif len(temp) > 1 and len(temp) % 2 == 0:
            middle_index = int(len(temp) / 2)
            prev_index = int(middle_index - 1)
            middle_value = (temp[middle_index] + temp[prev_index]) / 2
            if middle_value % 2 == 0:
                median_lst.append(int(middle_value))
            else:
                median_lst.append(middle_value)
    return median_lst


test_lst = [2, 1, 5, 7, 2, 0, 5]
print(median(test_lst))