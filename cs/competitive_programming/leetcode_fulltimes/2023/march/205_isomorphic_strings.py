class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False

        def helper(s1, s2, store):

            for i in range(len(s1)):
                if(s1[i] not in store):
                    store[s1[i]]=s2[i]
                else:
                    if(store[s1[i]]!=s2[i]):
                        return False
            return True

        return ((helper(s,t,{})) and helper(t,s,{}))
