from math import sqrt

training_data = [
    [10, 15, 45],
    [11, 6, 37],
    [12, 14, 48],
    [7, 9, 33],
    [9, 14, 38],
    [8, 12, 40],
    [6, 11, 35],
    [15, 10, 50],
    [14, 8, 46],
    [7, 12, 35],
    [10, 6, 36],
    [13, 8, 44],
    [9, 7, 32],
    [5, 8, 30],
    [5, 10, 30]
]

datapoint = [7, 8]

for i in range(len(training_data)):
    cost = (training_data[i][0] - datapoint[0]) ** 2 + (training_data[i][1] - datapoint[1]) ** 2
    cost = sqrt(cost)
    training_data[i].append(cost)
    print(training_data[i])

k = 3
ans = 0

training_data.sort(key=lambda x: x[3])

for i in range(k):
    ans += training_data[i][2]

ans /= k

print(ans)