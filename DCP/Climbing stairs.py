#Runtime is O(2**n)
def climb(n):
    if n <= 1:
        return n
    return climb(n - 1) + climb(n - 2)
def stairways(s):
    return climb(s + 1)

print(stairways(4))

#Runtime is O(x**n)



