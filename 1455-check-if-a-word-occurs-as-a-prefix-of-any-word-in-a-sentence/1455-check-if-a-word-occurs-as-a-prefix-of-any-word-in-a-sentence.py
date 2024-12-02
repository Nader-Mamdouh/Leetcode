class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst=sentence.split(" ")
        for index , word in enumerate(lst):
            s=""
            for ch in word:
                s+=ch
                if s==searchWord:
                    return index+1
        return -1            
