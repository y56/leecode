###### tags: `leetcode`

# 121. Best Time to Buy and Sell Stock

## Brute Force
time: $\Theta ( n^2 )$
space: $\Theta ( 1 )$
```python=
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Brute Force
        # time: n^2
        
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit
                    
                    
```
## Linear Update
time: $\Theta ( n )$
space: $\Theta ( 1 )$ 
```python=
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        cur_min = prices[0]
        cur_max = prices[1]
        
        for i in range(0, len(prices) - 1):
            if prices[i] < cur_min:  # Always false for the 1st time.
                cur_min = prices[i]
            if prices[i+1] - cur_min > max_profit:
                cur_max = prices[i+1]
                max_profit = cur_max - cur_min
            
        return max_profit
```
Note that, when the algorithm finishes, the `cur_min` may not be the value who produces `max_profit`, while the `cur_max` is always the value who produces `max_profit`.