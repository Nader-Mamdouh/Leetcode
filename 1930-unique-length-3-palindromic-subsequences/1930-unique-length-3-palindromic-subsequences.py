class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic=defaultdict(list)
        n=len(s)
        ans=0
        for i in range(n):
            dic[s[i]].append(i)
        for key,value in dic.items():
            arr=value
            first=arr[0]
            last=arr[-1]
            st=set()      
            for j in range(first+1,last):
                #print(f"{s[first]}{s[j]}{s[last]}")
                st.add(s[j])
            ans+=len(st) 
        return ans       
                
