class Solution:
    def decodeString(self, s: str) -> str:
        #s="10[leetcode]"
        stack=[]
        for i in range(len(s)):
            if s[i]=="]":
                s2=""
                n=""
                while(stack[-1]!="["):
                    s2+=stack[-1]
                    stack.pop()
                stack.pop()
                s2=s2[::-1]
                while (len(stack)>0 and stack[-1].isdigit() ):
                    n+=stack[-1]
                    stack.pop()
                n=n[::-1]
                limit=int(n)
                
                for i in range(limit):
                    stack.append(s2)
            else:
                stack.append(s[i])
        ans=""
        for i in stack:
            ans+=i
        return(ans)