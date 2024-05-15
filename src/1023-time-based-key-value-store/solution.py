from collections import defaultdict
class TimeMap:

    def __init__(self):
        # list of (value, timestamp), by default empty list for val in key: val
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """
        Note that the timestamps added to the store is in ascending order.
        This is because as time passes, the next time added is always bigger.
        For example: if time of 1 second passes, the store now has k,v = 1. Then 
        4 seconds has to pass for the next time I can add to the store, so its k, v = 4.

        This lets us do binary search, searching in an array of arrays of time stamps and values.
        Now we have to find the value closest to the timestamp in get(), so its similar to minimum in rotated sorted
        array, but the array ain't rotated

        Time: O(log n)
        Space: O(n)
        """
        arr = self.store[key]
        res = ""
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            store_value, store_timestamp = arr[middle]

            if store_timestamp <= timestamp:
                # we want to get as close as possible to timestamp
                # since right side are bigger numbers, we can afford to go bigger
                # since we now have a value less than timestamp
                res = store_value
                left = middle + 1
            else:
                # we are too big, timestamp too big
                # go smaller
                right = middle - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
