from collections import defaultdict
class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        ans = []
        dic = defaultdict(list)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                div = arr[i] / arr[j]
                ans.append(div)
                dic[div] = [arr[i], arr[j]]
        ans.sort()

        return dic[ans[k-1]]
