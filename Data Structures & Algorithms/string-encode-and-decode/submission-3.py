class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs: 
            encodedString += str(len(word)) + "#" + word
        return encodedString
                

    def decode(self, s: str) -> List[str]:
        word = []
    

        index = 0
        
        while index < len(s): 
            length = ""
            while s[index] != "#":
                length += s[index]
                index += 1
            length = int(length)
            word.append(s[index+1:index+1 + length])
            index += length + 1

        return word



        
            
