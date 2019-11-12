class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        def findMax(nums): #以复杂度n遍历寻找当前最优解
            res=[nums[0]]
            allLen=[]
            for i in range(1,len(nums)):
                if(nums[i] <= res[-1]):
                    if(len(res)>1):
                        if(nums[i] > res[-2]):
                            res[-1]=nums[i]
                        else:
                            continue
                    else:
                        res[-1]=nums[i]
                else:
                    res.append(nums[i])
            return len(res)
        allI = []
        for i in range(0,len(nums)): #选择可能存在的起点
            if(nums[i]<nums[0]):
                allI.append(i)
        allLen = []
        allLen.append(findMax(nums))
        for i in allI:
            allLen.append(findMax(nums[i:])) #对所有可能的起点进行求值，取max
        return max(allLen)