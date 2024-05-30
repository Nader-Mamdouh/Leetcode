class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        total = 0
        prefix = [0] * (len(arr) + 1)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]
        for i in range(1, len(prefix)):
            for j in range(i + 1, len(prefix)):
                for k in range(j, len(prefix)):
                    if (prefix[i - 1] ^ prefix[j - 1]) == (prefix[j - 1] ^ prefix[k]):
                        total += 1
        return total
