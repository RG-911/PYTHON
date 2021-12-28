import re

print(sum(list(map(int, re.findall("\d+", input())))))
