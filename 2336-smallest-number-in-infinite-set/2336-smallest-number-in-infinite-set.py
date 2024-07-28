class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1,1001)]
        heapify(self.nums)
        self.s = set(self.nums)
    def popSmallest(self) -> int:
        x = heappop(self.nums)
        self.s.remove(x)
        return x
    def addBack(self, num: int) -> None:
        if num in self.s:
            return None
        self.s.add(num)
        heappush(self.nums,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)