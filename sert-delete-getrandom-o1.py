
class RandomizedSet:

    def __init__(self):
        self.s={}
        self.pos=0
        self.a=[]
        

    def insert(self, val: int) -> bool:
        if val in self.a:
            return False
        else:
            self.s[val]=self.pos
            self.pos+=1
            self.a.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.a:
            return False
        else:
            self.s[self.a[-1]]=self.s[val]
            self.a[self.s[val]]=self.a[-1]
            self.a.pop()
            self.s.pop(val)
            self.pos-=1
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.a)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#method 2 using try-expect

class RandomizedSet:

    def __init__(self):
        self.s={}
        self.pos=0
        self.a=[]
        

    def insert(self, val: int) -> bool:
        try:
            self.s[val]
            return False
        except:
            self.s[val]=self.pos
            self.pos+=1
            self.a.append(val)
            return True

    def remove(self, val: int) -> bool:
        try:
            self.s[val]
            self.s[self.a[-1]]=self.s[val]
            self.a[self.s[val]]=self.a[-1]
            self.a.pop()
            self.s.pop(val)
            self.pos-=1
            return True
        except:
            return False
        

        

    def getRandom(self) -> int:
        return random.choice(self.a)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
