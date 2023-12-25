class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_str_odd, longest_str_even = s[0], s[0]
        
        
        
        for i in range(len(s)):
            
            print("YES")
            l = i-1
            r = i+1
            
            current_string = s[i]
            longest_str_odd = self.returnPalindromeString(current_string, longest_str_odd, l,r,s)
                

        for i in range(len(s)):
            
            l = i
            r = l+i
            
            current_string = ""
            longest_str_even = self.returnPalindromeString(current_string, longest_str_even, l,r,s)
            
        if len(longest_str_even) >= len(longest_str_odd):
            return longest_str_even
        else:
            return longest_str_odd 
    
    def returnPalindromeString(self, current_string, out_str, l, r, s):
        
        while( l>= 0 and r < len(s)  and s[l] == s[r] and l != r):
            
            current_string = s[l] + current_string + s[r]
            # current_string = s[l] + current_string + s[r]


            if len(current_string) >= len(out_str):

                out_str = current_string

            l -= 1
            r += 1
        
        return out_str

        
            
            
    