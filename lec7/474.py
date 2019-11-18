class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #返回0，1数量
        # def cal0And1(item):
        #     nums=[0,0]
        #     for num in item:
        #         if(int(num)==0):
        #             nums[0]+=1
        #         else:
        #             nums[1]+=1
        #     return nums

        if len(strs) == 0:
            return 0
        #定义dp数组
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]   
        
        for strs_item in strs:
            item_count0 = strs_item.count('0')
            item_count1 = strs_item.count('1')
            
            #遍历可容纳的背包 
            for i in range(m, item_count0 - 1, -1):  #采取倒序
                for j in range(n, item_count1 - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-item_count0][j-item_count1])
                    
        return dp[m][n]