  class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=len(numbers)-1
        i=0
        while i<l:
            s=numbers[i]+numbers[l]
            if s==target:
                return [i+1,l+1]
            elif s>target:
                l-=1
            else:
                i+=1
            
