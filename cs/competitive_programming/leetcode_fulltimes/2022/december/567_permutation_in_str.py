class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2): return False
        s1_cnt, s2_cnt = [0]*26, [0]*26

        for i in range(len(s1)):
            s1_cnt[ord(s1[i])-ord('a')] += 1
            s2_cnt[ord(s2[i])-ord('a')] += 1
        
        matches = 0

        for i in range(26):
            if s1_cnt[i]==s2_cnt[i]:
                matches += 1
        
        # Sliding Window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches==26:
                return True
            
            index = ord(s2[r])-ord('a')
            s2_cnt[index] += 1
            if s2_cnt[index]==s1_cnt[index]:
                matches += 1
            elif s2_cnt[index]-1==s1_cnt[index]:
                matches -= 1

            index = ord(s2[l])-ord('a')
            s2_cnt[index] -= 1
            if s2_cnt[index]==s1_cnt[index]:
                matches += 1
            elif s2_cnt[index]+1==s1_cnt[index]:
                matches -= 1
            
            l += 1
            
        return matches==26