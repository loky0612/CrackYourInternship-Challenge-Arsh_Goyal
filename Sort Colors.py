class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]