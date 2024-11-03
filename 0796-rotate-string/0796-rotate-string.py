class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)):
            if s[i]==goal[0]:
                news=s[i:]+s[:i]
                print(news)
                if news==goal:
                    return True
                else:
                    return False   
        return False             