def profit(lst):
    max_value = max(lst)
    min_val = min(lst)
    max_idx = lst.index(max_value)
    min_idx = lst.index(min_val)
    if min_idx < max_idx:
        max_profit = max_value - min_val
        return max_profit
    else:
        max_after_min = max(lst[min_idx:])
        min_before_max = min(lst[:max_idx + 1])
        p1 = max_after_min - min_val
        p2 = max_value - min_before_max
        if p1 > p2:
            return p1
        else:
            return p2

L = [9, 28, 8, 5, 7, 10]
print(profit(L))