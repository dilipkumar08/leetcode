class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
      li = [str(i) for i in range(1,10)]
      for _ in range(n-1):
        n = len(li)
        for i in range(n):
          num = li.pop(0)
          number = int(num[-1])
          
          if(number+k<=9):
            li.append(str(num) + str(number+k))
          
          if(number>=k and str(num) + str(number-k) not in li):
            li.append(str(num) + str(number-k))
        
      return li
