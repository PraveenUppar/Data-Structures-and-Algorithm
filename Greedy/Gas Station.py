# There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

# gas[i] is the amount of gas at the ith station.
# cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
# You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

# It's guaranteed that at most one solution exists.

def station(gas, cost):

    if sum(gas) < sum(cost):
        return - 1

    total_gas = 0
    start = 0

    for i in range(len(gas)):

        total_gas = (total_gas + gas[i]) - cost[i]

        if total_gas < 0:
            total_gas = 0
            start += 1

    return start