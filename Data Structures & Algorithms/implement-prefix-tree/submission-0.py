class PrefixTree:

    def __init__(self):
        self.root = [None] * 26
        self.end = False

    def insert(self, word):
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.root[idx] is None:
                node.root[idx] = PrefixTree()
            node = node.root[idx]
        node.end = True

    def search(self, word):
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.root[idx] is None:
                return False
            node = node.root[idx]
        return node.end

    def startsWith(self, prefix):
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.root[idx] is None:
                return False
            node = node.root[idx]
        return True