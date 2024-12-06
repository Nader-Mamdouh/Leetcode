class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l=0
        r=len(products)-1
        ans=[]
        for i in range(len(searchWord)):
            search=searchWord[i]

            while l<=r and (len(products[l])<=i or products[l][i]!=search):
                l+=1
            while l<=r and (len(products[r])<=i or products[r][i]!=search):
                r-=1
            words_left=r-l+1
            if words_left>=3:
                ans.append(products[l:l+3])   
            else:
                ans.append(products[l:r+1]) 
        return ans            