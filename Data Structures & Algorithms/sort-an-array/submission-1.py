class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1): # bởi vì nếu không -1 thì j + 1 sẽ bị out of index, - i thì do không cần những giá trị cuối nữa vì nó đã được sort và chắc chắn lớn nhất rồi
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
        