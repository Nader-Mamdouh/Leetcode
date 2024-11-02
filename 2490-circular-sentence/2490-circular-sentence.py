class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst=sentence.split(" ")
        if len(lst)==1:
            if lst[0][0]!=lst[0][-1]:
                return False
        for i in range(len(lst)):
            
            if i==len(lst)-1:
                continue
            else:
                if lst[i][-1]!=lst[i+1][0]:
                    return False
        if lst[0][0]!=lst[-1][-1]:
            return False             
        return True            
