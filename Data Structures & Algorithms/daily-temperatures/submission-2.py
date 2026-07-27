class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result : list[int] = [0] * len(temperatures)
        stack : list[(int, int)] = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                remove_index = stack.pop()[1]
                result[remove_index] = i - remove_index
            stack.append((temperatures[i], i))
        return result
            
                
              
