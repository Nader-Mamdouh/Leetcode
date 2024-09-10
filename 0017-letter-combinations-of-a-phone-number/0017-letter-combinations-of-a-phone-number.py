class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits:
            return []  
        result = []
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return
            current_digit = digits[index]
            for letter in dic[current_digit]:
                backtrack(index + 1, current_combination + letter)
        backtrack(0, "")     
        return result
