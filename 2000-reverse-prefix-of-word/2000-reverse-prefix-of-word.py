class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=""
        for i in range(len(word)):
            if word[i]==ch:
                s=(word[:i+1][::-1] + word[i+1:])
                return s
                
        return word        
                