class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_cost > total_gas:
            return -1
        
        start = 0
        gas_so_far = 0
        for i in range(len(gas)):
            gas_so_far += gas[i] - cost[i]

            if gas_so_far < 0:
                start = i + 1
                gas_so_far = 0


        return start
