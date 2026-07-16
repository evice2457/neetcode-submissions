class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        result = 0 
        while i < j: 
            width = j - i
            height = min(heights[i], heights[j])
            result = max(result, width * height)
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return result
