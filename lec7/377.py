class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if(not nums): return 0
        dp=[0]*(target+1)
        dp[0]=1
        nums.sort()
        #依次更新dp数组：分别以nums中的数依次开头
        for i in range(1,target+1):
            for j in range(0,len(nums)):
                if(nums[j]<=i):
                    dp[i]+=dp[i-nums[j]]
        return dp[-1]