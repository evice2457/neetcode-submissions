class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in dictionary:
            count = dictionary[num]
            buckets[count].append(num)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(result) >= k:
                break
            result.extend(buckets[i])
        return result
