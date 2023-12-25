#!/usr/bin/python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str_odd = s[0]
        longest_str_even = s[0]
        odd_palin = ""
        even_palid = ""


        for i in range(len(s)):
            l = i-1
            r = i+1

            current_string = s[i]

            while(l >= 0 and r < len(s) and s[l] == s[r]):
                current_string = s[l] + current_string + s[r]
                if len(current_string) >= len(longest_str_odd):
                    longest_str_odd = current_string
                l -= 1
                r += 1


        for i in range(len(s)):
            l = i
            r = l+1

            current_string = ""

            while(l >= 0 and r < len(s) and s[l] == s[r]):
                current_string = s[l] + current_string + s[r]

                if len(current_string) >= len(longest_str_even):
                    longest_str_even = current_string

                l = l-1
                r = r+1

        if len(longest_str_even) >= len(longest_str_odd):
            return longest_str_even
        else:
            return longest_str_odd 