class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2 != 0 or len(nums)<=1):
            return False
        else:
            #构建背包数组
            high = len(nums)
            size = int(sum(nums)/2)
            allSituation = [[0 for j in range(0,size+1)] for i in range(0,high)]
            #初始化第一行
            for i in range(1,size+1):
                if(i>=nums[0]):
                    allSituation[0][i]=nums[0]
                else:
                    allSituation[0][i]=0
            #填充所有情况
            for i in range(1, high):
                for j in range(nums[i], size+1):
                    allSituation[i][j]=max(allSituation[i-1][j],allSituation[i-1][j-nums[i]]+nums[i])
                    if(allSituation[i][j] == size):
                        return True
            return False