class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        for i in range(len(strs[0])):

            for s in strs:
                if(i==len(s) or s[i]!=strs[0][i]):
                    return res

            res += strs[0][i]
        return res
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_str = ""
        l = math.inf

        for str_a in strs:
            if len(str_a)==0:
                return ""
            if len(str_a)<l:
                short_str = ""
                short_str = str_a
                l = len(str_a)

        
        for i in range(len(short_str)+1):
            out = short_str[:i]

            for str_a in strs:
                if str_a.startswith(out):
                    continue
                else:
                    return out[:i-1]
        
        return out