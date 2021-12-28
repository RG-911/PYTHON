def pol_sub_str(word):
    lower = word.lower()
    lower_rev = lower[:: -1]
    if lower_rev == lower:
        print(lower)
        print(lower_rev)
    else:
        for i in range(len(word)):
            if lower[i:] == lower_rev[: -i]:
                return lower_rev[: -i]

            elif lower[:(len(word) - i)] == lower_rev[i:]:
                return lower[:len(word)]

            elif lower[i: len(word) - i] == lower_rev[i: len(word) - i]:
                return lower[i: len(word) - i]


L = "aabcdcb"
S = "bananas"

print(pol_sub_str(L))
print(pol_sub_str(S))

