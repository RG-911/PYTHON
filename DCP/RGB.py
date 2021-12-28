def char(l):
    indices = []
    temp = []
    for i in range(len(l)):
        if l[i] == 'R':
            indices.append(i)
    for k in range(len(l)):
        if l[k] == 'G':
            indices.append(k)
    for g in range(len(l)):
        if l[g] == 'B':
            indices.append(g)
    #return indices
    for j in range(len(indices)):
        r = indices[j]
        temp.append(l[r])
    return temp

lst = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(char(lst))
