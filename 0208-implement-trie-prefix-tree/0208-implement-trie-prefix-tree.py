class Trie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        current = self
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Trie()  
            current = current.children[ch]
        current.is_end_of_word = True  

    def search(self, word: str) -> bool:
        current = self
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end_of_word  

    def startsWith(self, prefix: str) -> bool:
        current = self
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True  
