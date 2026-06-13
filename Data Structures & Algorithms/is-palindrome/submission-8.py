class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for i in s:
            if i.isalnum() == True:
                clean.append(i.lower())
        i = 0 
        j = len(clean) - 1
        while i < j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        return True