#method-1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero,one,two=[],[],[]
        for i in nums:
            if i==0:
                zero.append(i)
            elif i==1:
                one.append(i)
            else:
                two.append(i)
        nums[:]=zero+one+two

       
#method-2
def qs(li):
    if len(li)<2:
        return li
    elif len(li)==2:
        if li[0]>li[1]: 
            return [li[1],li[0]]
        else: return li
    else:
        mid=li[0]
        low=[x for x in li[1:] if x<=mid]
        high=[y for y in li[1:] if y>mid]
        print(low,mid,high)
        return qs(low)+[mid]+qs(high)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums[:]=qs(nums)
