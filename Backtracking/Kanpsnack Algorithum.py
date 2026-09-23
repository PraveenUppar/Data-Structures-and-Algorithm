# Given a set of items, each with a weight and a value, the goal is to determine the combination of items to include in a knapsack 
# so that the total weight does not exceed a given capacity limit (W) and the total value is maximized


def knapsnack(weights, values, capacity):

    max_val = 0

    def explore(i, curr_weight, curr_val):

        if i == len(weights):
            if curr_val > max_val:
                max_val = curr_val 
            return

        # exclude
        explore(i + 1, curr_weight, curr_val)

        # include
        if curr_weight + weights[i] <= capacity:
            explore(i + 1, curr_weight + weights[i], curr_val + values[i]) 

    explore(0,0,0)
    return max_val