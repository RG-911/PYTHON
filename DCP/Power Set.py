def p_s(S):
    r = [[]]
    for e in S:
        r += [x + [e] for x in r]

    return r


R = {1, 2, 3, 4}
#p_s(R)
print(p_s(R))