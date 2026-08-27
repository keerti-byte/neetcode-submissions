class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            n = len(i)
            encode = encode + str(n) + "#" + i
        return encode
    def decode(self, s: str) -> List[str]:
       decode = []
       i = 0
       while i < len(s):
        j = s.find('#', i)
        length = int(s[i:j])
        word = s[j+1 : j+length+1]
        decode.append(word)
        i = j + length + 1  
       return decode