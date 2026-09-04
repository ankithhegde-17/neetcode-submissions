class Solution:
    def mergeTriplets(self, triplets, target):
        x, y, z = target
        a = b = c = False

        for t in triplets:
            if t[0] > x or t[1] > y or t[2] > z:
                continue

            if t[0] == x:
                a = True
            if t[1] == y:
                b = True
            if t[2] == z:
                c = True

        return a and b and c