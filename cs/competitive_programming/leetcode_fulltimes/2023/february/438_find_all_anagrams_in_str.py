class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:


        def getDs(st):
            res=[0]*26

            for e in st:
                res[ord(e)-ord('a')]+=1
        
            return res

        n = len(p)
        out = []
        base = getDs(p)
        start = getDs(s[0:n])
        if(start==base):
            out.append(0)
        
        i=1
        prev=s[0]
        while(i<len(s)):

            #subtract
            idx=ord(prev)-ord('a')
            start[idx]-=1
            # if(start[idx])<0:
            #      start[idx]=0

            if((i+n-1)<len(s)):
                start[ord(s[i+n-1])-ord('a')]+=1
                if start==base:
                    out.append(i)
            else:
                return out

            prev=s[i]
            i+=1
        
        return out