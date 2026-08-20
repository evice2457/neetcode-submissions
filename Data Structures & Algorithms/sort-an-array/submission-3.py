class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n): 
            min_index = -1 
            for j in range(i,n):
                if nums[j] <= nums[min_index]:
                    min_index = j 
            nums[i] , nums[min_index] = nums[min_index] , nums[i]
        return nums