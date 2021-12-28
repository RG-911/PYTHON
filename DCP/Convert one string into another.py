def convert(str_1, str_2):
    l_1 = list(str_1)
    l_2 = list(str_2)
    new_l = []
    if len(l_1) < len(l_2):
        for i in range(len(l_1)):
            if l_1[i] != l_2[i]:
                new_l.append(l_2[i])
            else:
                new_l.append(l_1)
        for i in range(len(l_1), len(l_2)):
            new_l.append(l_2[i])
    else:
        for i in range(len(l_2)):
            if l_1[i] != l_2[i]:
                new_l.append(l_2[i])
            else:
                new_l.append(l_1)

    return ''.join(new_l)

print(convert('Ruslan', 'Laman'))