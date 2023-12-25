class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars) ==1:
            return 1

        
        start, end, count = 0, 0, 1

        for end in range(1, len(chars)+1):

            if end < len(chars) and chars[end] == chars[end-1]:
                count += 1
            else:
                #updating the chars string
                chars[start] = chars[end-1]

                start += 1
                if count>1:
                    for k in str(count):
                        chars[start] = k
                        start += 1
                count = 1
        
        chars = chars[:start]
        return start