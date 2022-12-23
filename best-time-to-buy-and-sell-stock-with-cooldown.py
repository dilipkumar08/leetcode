class Solution:
    def maxProfit(self, price: List[int]) -> int:
        if not price:
            return 0
        
        hold,cooldown=-price[0],-price[0]
        nothold=0

        for i in range(len(price)):
            hold=max(hold,nothold-price[i])
            nothold=max(nothold,cooldown)
            cooldown=hold+price[i]
        
        return max(cooldown,nothold)
