class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = {}
        for x in hand:
            count[x] = count.get(x, 0) + 1

        for x in sorted(count):
            while count[x] > 0:
                for y in range(x, x + groupSize):
                    if count.get(y, 0) == 0:
                        return False
                    count[y] -= 1

        return True