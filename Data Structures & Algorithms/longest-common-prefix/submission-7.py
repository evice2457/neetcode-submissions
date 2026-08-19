class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            check_let = strs[0][i]
            for letter in strs[1:]:
                if i >= len(letter) or letter[i] != check_let:
                    return ans
            ans += check_let
        return ans