#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0

    # sort the coins in descending order
    sorted_coins = sorted(coins, reverse=True)

    change = 0
    remaining_total = total

    for coin in sorted_coins:
        if remaining_total <= 0:
            break
        temp = remaining_total // coin
        change += temp
        remaining_total -= (temp * coin)

    if remaining_total != 0:
        return -1

    return change
