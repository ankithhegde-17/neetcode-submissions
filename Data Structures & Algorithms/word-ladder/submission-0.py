from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, d = q.popleft()

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nw = word[:i] + c + word[i + 1:]
                    if nw in words:
                        if nw == endWord:
                            return d + 1
                        words.remove(nw)
                        q.append((nw, d + 1))

        return 0