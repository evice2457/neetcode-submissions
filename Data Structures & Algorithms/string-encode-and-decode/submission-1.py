class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string +=  str(len(string)) + "#" + string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        num = 0
        decoded_strs = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            decoded_strs.append(s[j+1:j+1+num])
            j += 1 + num 
            i = j
        return decoded_strs