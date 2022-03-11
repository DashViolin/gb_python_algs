# https://leetcode.com/problems/replace-words/solution/
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        tokens = sentence.split()
        for index, _ in enumerate(tokens):
            for root in dictionary:
                if tokens[index].startswith(root):
                    tokens[index] = root
        return ' '.join(tokens)
