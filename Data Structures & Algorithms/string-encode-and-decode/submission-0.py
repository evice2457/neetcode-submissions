class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string +=  str(len(string)) + "#" + string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        decoded_strs = []
        num = 0
        while j < len(s): 
            if s[i:j].isdigit() and s[j] == "#":
                num = int(s[i:j])
                decoded_strs.append(s[j+1:j+1+num])
                j += num + 1
                i = j
            else:
                j += 1
        return decoded_strs