"""
Time Limit Exceeded
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:


        len_t = len(t)
        len_s = len(s)
        res = []

        def encode(s):

            # lower case:
            #   start: 0 and end:25
            # upper case:
            #   start: 26 and end:51

            res = [0]*52

            for c in s:
                # upper case
                if c.isupper():
                    idx = ord(c)-ord('A')+26
                # lower case
                else:
                    idx = ord(c)-ord('a')
                res[idx] += 1
            
            return res

        t_encode = encode(t)

        def compare(encode_s, encode_t):

            for i in range(52):
                if( (encode_t[i]>0) and (encode_s[i]<encode_t[i])):
                    return False
                elif((encode_t[i]>=0) and (encode_s[i]>=encode_t[i])) :
                    continue
            return True
        
        def generateStrs(l,r):

            tmp=""
            if(l>=0 and r<len_s):
                if l==r:
                    tmp+=s[l]
                else:
                    tmp+=(s[l]+s[r])
                l-=1
                r+=1

            if(len(tmp)>=len_t):
                if(compare(encode(tmp), t_encode)):
                    res.append(tmp)

            while(l>=0 and r<len_s):

                tmp = s[l] + tmp
                tmp = tmp + s[r]

                if(len(tmp)>=len_t):
                    if(compare(encode(tmp), t_encode)):
                        res.append(tmp)

                l -= 1
                r += 1





        for i in range(0, len_s):

            #even
            generateStrs(i,i+1)


            #odd
            generateStrs(i,i)


        if len(res)==0:
            return ""

        result = res[0]

        for ele in res[1:]:
            if len(ele)<len(result):
                result=ele

        return result

        



class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""
        t_store, s_store = {}, {}

        for c in t:
            t_store[c] = 1 + t_store.get(c, 0)
        
        have, need = 0, len(t_store)    
        l,r=0,0
        res, resL = [-1,-1], float('inf')


        for r in range(len(s)):

            c = s[r]
            s_store[c] = 1 + s_store.get(c,0)

            if ((c in t_store) and (s_store[c]==t_store[c])):
                have += 1

            while(have==need):

                # update our result
                curr_len = r-l+1
                if(curr_len<resL):
                    res = [l,r]
                    resL = curr_len

                # pop from left of our window
                rmv_c = s[l]
                s_store[rmv_c]-=1

                if( (rmv_c in t_store) and (s_store[rmv_c]<t_store[rmv_c])):
                    have -= 1
                
                l += 1

        l,r = res 
        return s[l:r+1] if resL!=float('inf') else ""