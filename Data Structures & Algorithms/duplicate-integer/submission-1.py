from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = Counter(nums)
        for key, value in dictionary.items():
            if value > 1:
                return True
        return False