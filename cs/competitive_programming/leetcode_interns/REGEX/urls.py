#!/usr/bin/python3

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://murali.com
'''

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# pattern = re.compile(r'https?://(www\.)?[a-z]+\.(com|gov)')

pattern = re.compile(r'https?://(www\.)?([a-z]+\.)(com|gov)')

matches = pattern.finditer(urls)

result = pattern.sub(r'\2\3', urls)

print(result)


# print(matches)

# for x in matches:
#     print(x)

# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))