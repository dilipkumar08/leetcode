class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        lib=dict()
        a=list()
        for i in nums:
            if i==0:
                lib[i]=nums.count(i)

            if i%2==0:
                lib[i]=nums.count(i)
        if len(lib)==0:
            return -1
        else:
            for key,values in lib.items():
                if values==max(lib.values()):
                    a.append(key)
        return(min(a))
