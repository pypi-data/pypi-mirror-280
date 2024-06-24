import math

def euclidean_dist(x, y):
    total_sum = 0.0
    for i in range(len(x)):
        diff = x[i] - y[i]
        squared_diff = diff ** 2
        total_sum += squared_diff
    distance = math.sqrt(total_sum)
    return distance

def taxicab_dist(x, y):
    total_sum = 0.0
    for i in range(len(x)):
        diff = abs(x[i] - y[i])
        total_sum += diff
    return total_sum

def supremum_dist(x, y):
    max_diff = 0.0
    for i in range(len(x)):
        diff = abs(x[i] - y[i])
        if diff > max_diff:
            max_diff = diff
    return max_diff

def minkowski_dist(x, y, p=2):
    total_sum = 0.0
    p = float(p)
    for i in range(len(x)):
        diff = abs(x[i] - y[i])
        powered_diff = diff ** p
        total_sum += powered_diff
    distance = total_sum ** (1/p)
    return distance
