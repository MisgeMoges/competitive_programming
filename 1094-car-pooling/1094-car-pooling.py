class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        numberOfTrips = [0]*1001
        for trip, i, j in trips:
            numberOfTrips[i] += trip
            numberOfTrips[j] -= trip
        carLoad = 0
        for i in range(len(numberOfTrips)):
            carLoad += numberOfTrips[i]
            if carLoad > capacity:
                return False
        return True