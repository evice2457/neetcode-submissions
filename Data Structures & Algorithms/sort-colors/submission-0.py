class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dictionary = {
            "red" : 0,
            "white" : 0,
            "blue" : 0
        } 
        for num in nums:
            if num == 0:
                dictionary["red"] += 1
            elif num == 1:
                dictionary["white"] += 1
            else:
                dictionary["blue"] += 1
        result = [0] * dictionary["red"] + [1] * dictionary["white"] * 1 + [2] * dictionary["blue"]
        nums[:] = result
        