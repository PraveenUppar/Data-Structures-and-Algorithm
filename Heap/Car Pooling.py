# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and a integer array trips where trips[i] = [numPassengers[i], from[i], to[i]] indicates 
# that the ith trip has numPassengers[i] passengers and the locations to pick them up and drop them off are from[i] and to[i] respectively. 
# The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

def car(trips, capacity):

    locations = []

    for passenger, pickup, drop in trips:
        locations.append((pickup, passenger))
        locations.append((drop, passenger))

    locations.sort()
    curr_pass = 0

    for pickup, passenger in locations:
        curr_pass += passenger
        if curr_pass > capacity:
            return False 
    return True