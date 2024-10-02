class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_dict = {val: i + 1 for i, val in enumerate(sorted_arr)}
        return [rank_dict[num] for num in arr]
