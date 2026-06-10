from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for str in strs:
            char = Counter(str)
            char_tuple = tuple(sorted(char.items()))
            if char_tuple in dictionary:
                dictionary[char_tuple].append(str)
            else:
                dictionary[char_tuple] = [str]
        result = []
        for key in dictionary:
            result.append(dictionary[key])
        return result