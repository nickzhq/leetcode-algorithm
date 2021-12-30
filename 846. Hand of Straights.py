# coding=utf-8
# @Time     : 30th December, 2021  17:22
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : 846. Hand of Straights.py
# @Software : PyCharm 
# =======================================================

# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
# and consists of groupSize consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        d = Counter(hand)

        for x in hand:
            if d[x] == 0:
                continue

            for i in range(x, x+groupSize):
                if d[i] == 0:
                    return False
                d[i] -= 1

        return True
