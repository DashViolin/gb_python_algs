# https://leetcode.com/problems/replace-words/solution/

# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         tokens = sentence.split()
#         for index, _ in enumerate(tokens):
#             for root in dictionary:
#                 if tokens[index].startswith(root):
#                     tokens[index] = root
#         return ' '.join(tokens)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = word

    def replace(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                break
            curr = curr.children[char]
            if curr.word:
                return curr.word
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        return " ".join(map(trie.replace, sentence.split()))
