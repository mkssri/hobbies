class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        res = []
        target_dict = {}

        for c in target:
            if c not in target_dict:
                target_dict[c] = 0
            target_dict[c] += 1

        print("target_dict: {}".format(target_dict))

        for k,v in target_dict.items():
            cnt = s.count(k)
            if cnt>= v:
                res.append( cnt//v )
            else:
                res.append( 0 )
        
        return min(res)