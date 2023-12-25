class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for s in strs:
            res += str(len(s))+"#"+s
        
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        l, i, res = len(s), 0, []

        while(i<l):
            j = i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res