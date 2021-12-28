def invers(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                count += 1
    return count
L = [2, 4, 1, 3, 5]
T = [5, 4, 3, 2, 1]
print(invers(L))
print(invers(T))