class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        st, ed = 0, len(s)-1
        lst = list(s)

        while( st<ed ):

            if(lst[st] in vowels):
                tmp = lst[st]

                while(lst[ed] not in vowels):
                    ed -= 1
                
                if(ed<st):
                    return "".join(lst)
                
                lst[st] = lst[ed]
                lst[ed] = tmp
                ed -= 1
            st += 1

        return "".join(lst)