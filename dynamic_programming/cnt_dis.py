import timeit

# Count number of ways to cover a distance

def countWayCoverD(distance):
    if (distance < 3):
        return distance
    elif (distance == 3):
        return 4

    return countWayCoverD(distance-1) + countWayCoverD(distance-2) + countWayCoverD(distance-3)


def countWayCoverDBottomup(distance):
    distance_arr = [0]*(distance+1)
    distance_arr[1] = 1
    distance_arr[2] = 2
    distance_arr[3] = 4

    for i in range(4, distance + 1):
        distance_arr[i] = distance_arr[i-1] + distance_arr[i-2] + distance_arr[i-3]

    return distance_arr[distance]
    

start = timeit.default_timer()
distance = 30
print(countWayCoverD(distance))
stop = timeit.default_timer()
print('Eslaped Time naive: ', stop - start)

start = timeit.default_timer()
distance = 30
print(countWayCoverDBottomup(distance))
stop = timeit.default_timer()
print('Eslaped Time DP bottom up: ', stop - start)
