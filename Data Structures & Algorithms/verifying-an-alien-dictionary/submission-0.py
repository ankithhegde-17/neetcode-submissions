class Solution:
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}
        return all(
            [rank[c] for c in a] <= [rank[c] for c in b]
            for a, b in zip(words, words[1:])
        )