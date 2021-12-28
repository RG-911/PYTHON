def connections(lst):
    start = input()
    flights = []
    departures = []
    destinations = []
    for tup in lst:
        departures.append(tup[0])
        destinations.append(tup[1])
    if start in departures:
        flights.append(start)

    for i in range(len(lst)):
        if flights[-1] in departures:
            idx = departures.index(flights[-1])
            temp_dep = departures[idx]
            temp_des = destinations[idx]
            flights.append(temp_des)
            departures.pop(idx)
            destinations.pop(idx)
        else:
            return 0

    return flights


trips_1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
trips_2 = [('SFO', 'COM'), ('COM', 'YYZ')]
trips_3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
print(connections(trips_1))
print(connections(trips_2))
print(connections(trips_3))