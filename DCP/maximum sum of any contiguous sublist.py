def max_sum(lst):
    sum = 0
    for el in lst:
        sum += el
        if sum < 0:
            sum = 0
    return sum




L =  [34, -50, 42, 14, -5, 86]
K =  [-5, -1, -8, -9]
print(max_sum(L))
print(max_sum(K))