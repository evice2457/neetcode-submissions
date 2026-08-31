class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        result = []
        for key, value in count.items():
            if value > len(nums) // 3:
                result.append(key)
        return result