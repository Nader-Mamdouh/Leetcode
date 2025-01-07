class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lst=[]
        words.sort()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i!=j:
                    lst.append(words[i])
                    break
        return lst
            