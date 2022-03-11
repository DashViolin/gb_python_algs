# https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/
from collections import defaultdict
import re


class WordDictionary:
    def __init__(self):
        self.words = defaultdict(set)

    def addWord(self, word: str) -> None:
        if word:
            self.words[len(word)].add(word)

    def search(self, word: str) -> bool:
        if word:
            word = word.lower()
            if not '.' in word:
                return word in self.words.get(len(word), set())
            else:
                pattern = re.compile(f'^{word}$')
                for w in self.words.get(len(word), set()):
                    if bool(re.search(pattern, w)):
                        return True
        return False


# ------------------------------------------------------------

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.value = ""


class WordDictionaryByTier:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word.lower():
            child = node.children.get(char)
            if child is None:
                child = TrieNode()
                node.children[char] = child
            node = child
        node.is_word = True

    def search(self, word):
        def next_char(root, word):
            if len(word) == 0:
                return root.is_word
            elif word[0] == '.':
                for node in root.children:
                    if next_char(root.children[node], word[1:]):
                        return True
                return False
            else:
                node = root.children.get(word[0])
                if node is None:
                    return False
                return next_char(node, word[1:])

        return next_char(self.root, word.lower())

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
