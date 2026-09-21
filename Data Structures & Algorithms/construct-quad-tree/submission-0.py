"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid):
        def build(r, c, size):
            if size == 1:
                return Node(bool(grid[r][c]), True)

            half = size // 2

            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)

            children = [topLeft, topRight, bottomLeft, bottomRight]

            if all(x.isLeaf for x in children) and all(x.val == children[0].val for x in children):
                return Node(children[0].val, True)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, len(grid))