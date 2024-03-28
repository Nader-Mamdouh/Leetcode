class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruitCount = {}
        start = 0
        maxFruits = 0
        
        for end in range(len(fruits)):
            fruitCount[fruits[end]] = fruitCount.get(fruits[end], 0) + 1
            
            while len(fruitCount) > 2:
                fruitCount[fruits[start]] -= 1
                if fruitCount[fruits[start]] == 0:
                    del fruitCount[fruits[start]]
                start += 1
            
            maxFruits = max(maxFruits, end - start + 1)
        
        return maxFruits
        