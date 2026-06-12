class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dictionary = {}
        for num in nums:
            prior = num - 1
            if prior not in nums:
                dictionary[num] = []
        for key in dictionary:
            count = 0
            while True:
                check_num = int(key) + count
                if check_num in nums:
                    dictionary[key].append(check_num)
                    count += 1
                else:
                    break
        return max(len(v) for v in dictionary.values())
        