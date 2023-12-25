class Solution:
    def isPalindrome(self, x: int) -> bool:

        st = 0
        x=str(x)
        en = len(x)-1

        while(st<en):
            if(x[st]!=x[en]):
                return False
            st += 1
            en -= 1
        
        return True