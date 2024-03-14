#!/usr/bin/python3
""" Prime number game """


def isWinner(x, nums):
    """ check for the winner of the prime number game"""
    if not nums or x < 1:
        return None
    max_n = max(nums)

    filter_nums = [True for _ in range(max(max_n + 1, 2))]
    for i in range(2, int(pow(max_n, 0.5)) + 1):
        if not filter_nums[i]:
            continue
        # continue and do nothing
        for j in range(i * i, max_n + 1, i):
            filter_nums[j] = False
    filter_nums[0] = filter_nums[1] = False
    y = 0
    for i in range(len(filter_nums)):
        if filter_nums[i]:
            y += 1
        filter_nums[i] = y
    player_one = 0
    for x in nums:
        player_one += filter_nums[x] % 2 == 1
    if player_one * 2 == len(nums):
        return None
    if player_one * 2 > len(nums):
        return "Maria"
    return "Ben"
