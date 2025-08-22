class Trie:
    class Node:
        def __init__(self):
            self.nodes = [None] * 26
            self.is_end = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current_node.nodes[index] is None:
                current_node.nodes[index] = self.Node()
            current_node = current_node.nodes[index]
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            index = ord(char) - ord('a')
            current_node = current_node.nodes[index]
            if current_node is None:
                return False
        return current_node.is_end

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            current_node = current_node.nodes[index]
            if current_node is None:
                return False
        return True