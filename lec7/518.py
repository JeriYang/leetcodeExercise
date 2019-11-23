class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if(amount == 0): return 1
        elif(len(coins)==0): return 0
        dp=[0]*(amount+1)
        dp[0]=1
        for item in coins:
            for i in range(item,amount+1):
                dp[i] +=dp[i-item]
        return dp[amount];