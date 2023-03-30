class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        v=[]
        ind=[-1,-1]

        nums=[int(i) for i in nums]

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==(target-nums[j]):
                    return i,j