class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0: # then we cant go from i to i+1
                # Pick up the next station as the starting one.
                # also means starting_station~i are all illegal starts
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1

