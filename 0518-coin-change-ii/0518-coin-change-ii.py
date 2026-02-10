from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}  # key: (i, t) -> ways

        def dfs(i: int, t: int) -> int:
            # Base: only first coin available
            if i == 0:
                return 1 if t % coins[0] == 0 else 0

            # If already computed, return from memo
            if (i, t) in memo:
                return memo[(i, t)]

            # Not take current coin
            not_take = dfs(i - 1, t)

            # Take current coin (unlimited supply)
            take = 0
            if coins[i] <= t:
                take = dfs(i, t - coins[i])

            memo[(i, t)] = take + not_take
            return memo[(i, t)]

        if amount == 0:
            return 1
        if n == 0:
            return 0

        return dfs(n - 1, amount)


"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if amount == 0:
            return 1
        if n == 0:
            return 0

        # dp[i][t] = ways to make sum t using coins[0..i]
        dp = [[0] * (amount + 1) for _ in range(n)]

        # Base row: using only coins[0]
        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[0][t] = 1

        # Fill rest
        for i in range(1, n):
            for t in range(amount + 1):
                not_take = dp[i - 1][t]
                take = 0
                if coins[i] <= t:
                    take = dp[i][t - coins[i]]  # same row -> unlimited
                dp[i][t] = take + not_take

        return dp[n - 1][amount]

"""