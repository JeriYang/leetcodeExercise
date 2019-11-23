class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(len(coins)<=0): return -1
        elif(amount==0): return 0
        else:
            dp=[0]*(amount+1)
            coins.sort()
            #初始化res:
            for i in coins:
                if(i<=amount):
                    dp[i]=1
                else:
                    break
            print(coins)
            #计算dp数组
            leftMaxNum=[]
            for i in range(1,amount+1):
                if i in coins:
                    leftMaxNum.append(i)
                    continue
                else:
                    if(len(leftMaxNum)==0):continue
                    midNum=[]
                    for j in range(len(leftMaxNum)-1,-1,-1):
                        if(dp[i-leftMaxNum[j]]==0):
                            continue
                        else:
                            midNum.append(dp[i-leftMaxNum[j]])
                    if(len(midNum)>0):
                        dp[i]=1+min(midNum)

            if(dp[amount]==0):return -1
            else: return dp[amount]