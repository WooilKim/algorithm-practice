class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node(w)
            cur = cur.child[w]
        cur.child['*'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for w in word:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        if '*' in cur.child:
            return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for w in prefix:
            if w not in cur.child:
                return False
            cur = cur.child[w]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
def test(cmds, words):
    trie = Trie()
    for i in range(len(cmds)):
        if cmds[i] == 'insert':
            trie.insert(*words[i])
        elif cmds[i] == 'search':
            print(trie.search(*words[i]))
        elif cmds[i] == 'startsWith':
            print(trie.startsWith(*words[i]))


if __name__ == '__main__':
    cmds = ["insert", "search", "search", "startsWith", "insert", "search"]
    words = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    test(cmds, words)
