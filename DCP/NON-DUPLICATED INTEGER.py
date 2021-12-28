def unique(lst):
    for i in range(len(lst)):
        if lst[i] != lst[i + 1] and lst[i] != lst[i - 1]:
            return "This is a unique value: {} ".format(lst[i])


L = [6, 1, 3, 3, 3, 6, 6]
S = [13, 19, 13, 13]

print(unique(L))
print(unique(S))