def formula(lst, k):
    lst.sort()
    temp =[el for el in lst if el <= k]
    total_temp = sum(temp)
    dif = total_temp - k
    if dif in temp:
        idx = temp.index(dif)
        temp.pop(idx)
        return "The following combination of numbers " + str(temp) + " have sum of {} ". format(k)
    else:
        return "It is not possible to get {}". format(k)


S = [12, 1, 61, 5, 9, 2]
k = 24
print(formula(S, k))