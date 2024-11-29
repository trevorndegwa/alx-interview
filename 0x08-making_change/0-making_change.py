#!/usr/bin/python3
"""
function calculates the no. of coins
needed from a list of variable amounts of coins
to reach a total figure
"""


def makeChange(coins, total):
    """
    when given a pile of cons of different values,
    the function determines the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
