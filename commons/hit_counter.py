import time
import random

class HitCounter():
    """A hit counter using circular array
    N: last N seconds we want to keep the number of hits
    Assumption: number of hit per second < sys.maxsize of Python
    """
    def __init__(self, N=60):
        # Time: O(1)
        # Space: O(N)
        self.N = N
        self.counter = [(None, 0)] * self.N # a fixed size list of N tuples, \
                       # each tuple is (timestamp, number of hits)

    def log_hits(self):
        # Increase the existing hit counter of an item in the self.counter list
        # Time: O(1)
        # Space: O(1)
        epoch_time = int(time.time()) # current time
        i = epoch_time % self.N # where should we increase the hit in the list
        curr_timestamp, curr_hit = self.counter[i]
        # Case 1: initially, update the hit of a timestamp entry in the list to 1
        if curr_timestamp is None:
            self.counter[i] = (epoch_time, 1)
        # Case 2: when updating  an existing timestamp entry in the list
        # simply increase its hit count
        elif curr_timestamp == epoch_time: # when update an existing timestamp entry in the list
            self.counter[i] = (epoch_time, curr_hit + 1)
        # Case 3: when updating an old timestamp entry (curr_timestamp > timestamp )
        # simply reset its previous hit and start counting again (Case 2)
        else:
            self.counter[i] = (epoch_time, 1)

    def get_hit(self):
        # Time: O(N)
        # Space: O(N)
        # Aggregate hits from recent entries in the self.counter list
        epoch_time = int(time.time())
        res = 0
        # print(self.counter)
        for (item_timestamp, item_hit) in self.counter:
            if (item_timestamp is not None):
                    res += item_hit if ((epoch_time - item_timestamp) < self.N) else 0
        return res
