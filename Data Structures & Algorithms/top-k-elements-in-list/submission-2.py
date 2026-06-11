from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = Counter(nums)
        my_list = []
        for key,value in dictionary.items():
            my_list.append([value, key])
        new_list = sorted(my_list, reverse = True)
        result = [0] * k 
        for i in range(k):
            result[i] = new_list[i][1]
        return result
