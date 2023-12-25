class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        tmp = strs[0]

        for s in strs[1:]:
            if len(s)<len(tmp):
                tmp=s
        n = len(strs)
        l = len(tmp)

        tmp1=""

        for i in range(l):
            match = tmp[0:i+1]
            cnt = 0
            for s in strs:
                if s.startswith(match):
                    cnt += 1

            if cnt == n:
                tmp1 = match

        return tmp1
