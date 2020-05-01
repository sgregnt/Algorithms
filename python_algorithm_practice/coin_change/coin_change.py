"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""


# fewest number of coint to makeup that amount.

class Solution(object):
    def coinChange(self, coins, amount):
        # aaaa

        # first approach, get array as long the amount, then update locations with minimial numnber of coins going
        # upwaards.

        # okay run recursion and update hash with quantities you already had.

        tried = {}

        def backtracking(coins, amount):
            if amount == 0:
                return 0
            else:
                if amount in tried:
                    return tried[amount]
                else:
                    min_count = float('inf')
                    for coin in coins:
                        if coin <= amount:
                            count = 1 + backtracking(coins, amount - coin)
                            min_count = min([min_count, count])
                    tried[amount] = min_count

                return min_count
        count = backtracking(coins, amount)
        if count == float('inf'):
            return -1
        else:
            return count



a = Solution()
print(a.coinChange([1, 2, 5], 11))










