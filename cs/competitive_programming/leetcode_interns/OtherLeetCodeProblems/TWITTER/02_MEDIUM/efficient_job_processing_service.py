#!/usr/bin/python3

# Efficient Job Processing Service

def maximumTotalWeight(tasks, weights, runtime):
    items = [[tasks[i]*2,weights[i]] for i in range(len(tasks))]
    knapsackValues = [[0 for _ in range(runtime+1)] for _ in range(len(items)+1)]
    
    print("items - {}".format(items))
    print("knapsackValues - {}".format(knapsackValues))
    for i in range(1, len(items)+1):
        duration, value = items[i-1]
        for d in range(1, runtime+1):
            if duration > d:
                knapsackValues[i][d] = knapsackValues[i-1][d]
            else:
                knapsackValues[i][d] = max(knapsackValues[i-1][d], knapsackValues[i-1][d-duration]+value)
    print("knapsackValues - {}".format(knapsackValues))
    return knapsackValues[-1][-1]

tasks = [2,2,3,4]
runtime = 15
weights = [2,4,4,5]
out = maximumTotalWeight(tasks, weights, runtime)
print(out)

# items - [[4, 2], [4, 4], [6, 4], [8, 5]]

# knapsackValues - [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# knapsackValues - [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6], [0, 0, 0, 0, 4, 4, 4, 4, 6, 6, 8, 8, 8, 8, 10, 10], [0, 0, 0, 0, 4, 4, 4, 4, 6, 6, 8, 8, 9, 9, 10, 10]]
# 10