class LRUCache:

    def __init__(self, capacity: int):
        self.cashe = dict() 
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cashe:
            v = self.cashe[key]
            del self.cashe[key]
            self.cashe[key] = v
            return v
        else:
            return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cashe:
            del self.cashe[key]
        if len(self.cashe)==self.capacity:
            self.cashe.pop(next(iter(self.cashe)))
        self.cashe[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)