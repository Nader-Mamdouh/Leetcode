class RecentCounter:

    def __init__(self):
        self.p=0
        self.list=[]
        

    def ping(self, t: int) -> int:
        self.list.append(t)

        while abs(self.list[self.p]-self.list[-1])>3000:
            self.p+=1

        return (len(self.list)-1) - self.p +1
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)