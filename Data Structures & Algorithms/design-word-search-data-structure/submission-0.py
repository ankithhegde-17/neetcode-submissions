class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def addWord(self, word):
        node = self

        for ch in word:
            i = ord(ch) - ord('a')

            if node.children[i] is None:
                node.children[i] = WordDictionary()

            node = node.children[i]

        node.end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.end

            ch = word[i]

            if ch != '.':
                idx = ord(ch) - ord('a')

                if node.children[idx] is None:
                    return False

                return dfs(node.children[idx], i + 1)

            for child in node.children:
                if child and dfs(child, i + 1):
                    return True

            return False

        return dfs(self, 0)