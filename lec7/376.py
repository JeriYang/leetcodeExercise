class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        #贪心思想，建议画以一个X,Y轴，每次找最近的解
        maxLen = 0
        if(len(nums)<=1):
            return len(nums)
        if(len(nums)==2):
            if(nums[0]!=nums[1]):
                return 2
            else:
                return 1
        res = [nums[0]]
        pre = nums[0]
        for i in range(1,len(nums)-1):
            if(nums[i]>pre and nums[i]>nums[i+1]):
                pre = nums[i]
                res.append(nums[i])
            elif(nums[i]<pre and nums[i]<nums[i+1]):
                pre = nums[i]
                res.append(nums[i])
            else:
                continue
        #对最后一个数进行处理
        if(len(res)>1):
            if(res[-1] > res[-2] and res[-1]>nums[-1]):
                res.append(nums[-1])
            elif(res[-1] < res[-2] and res[-1]<nums[-1]):
                res.append(nums[-1])
        else:
            if(res[0]==nums[-1]):
                return 1
            else:
                res.append(nums[-1])
        return len(res)

            

            
