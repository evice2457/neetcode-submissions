from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        highest = float('-inf')
        result = 0
        for key in count:
            if count[key] >= highest:
                highest = count[key]
                result = key
        return result
