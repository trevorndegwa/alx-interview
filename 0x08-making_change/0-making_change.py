#!/usr/bin/python3
"""
function calculates the fewest number
of coins needed for a given total
"""


def makeChange(coins, total):
    """
    Determines the fewest no. of coins
    for a given total

    Parameters:
        coins (list): list of coins values available
        total (int): total amount to achieve
    Returns:
        int: fewest coins needed
    """
    if total <= 0:
        return 0

    # Initialise the DP table
    dp = [0] + [float("inf")] * total

    # Fill the DP table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float("inf") else -1
