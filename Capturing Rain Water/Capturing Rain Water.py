from time import time

####### TEST INPUTS HERE
small = [1, 0, 1]
medium = [4, 2, 1, 3, 0, 1, 2]
edge_case = [0, 2, 0]


####### NAIVE SOLUTION HERE
def rain_water(histogram):
    total_water = 0
    for i in range(1, len(histogram) - 1):
        left_values = histogram[:i]
        left_max = max(left_values)
        # print(left_values)
        print("Left max is: {0}".format(left_max))

        right_values = histogram[i:]
        right_max = max(right_values)
        # print(right_values)
        print("Right max is: {0}".format(right_max))

        fill_mark = min(right_max, left_max) - histogram[i]
        if fill_mark > 0:
            total_water += fill_mark
        print(total_water)


rain_water(medium)


####### OPTIMIZED SOLUTION HERE
def optimized_rain_water(histogram):
    total = 0
    max_value = histogram[0]
    left_maxes = []
    for i in range(len(histogram)):
        if histogram[i] > max_value:
            max_value = histogram[i]
        left_maxes.append(max_value)
    print(left_maxes)

    max_value = histogram[-1]
    right_maxes = []
    for i in range(1, len(histogram) + 1):
        if histogram[-i] > max_value:
            max_value = histogram[-i]
        right_maxes.append(max_value)
    right_maxes.reverse()
    print(right_maxes)

    for i in range(len(histogram) - 1):
        min_maxes = min(right_maxes[i], left_maxes[i]) - histogram[i]
        total += min_maxes
    print(total)


optimized_rain_water(medium)
####### BENCHMARKING HERE

