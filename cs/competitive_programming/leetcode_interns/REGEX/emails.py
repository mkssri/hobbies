#!/usr/bin/python3

import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey.schafer@|university.edu

corey-321-schafer@my-work.net
corey-321-schafer@|y-work.net
abc
'''

pattern = re.compile(r'[a-zA-Z0-9\.-]+@[a-z-]+\.(com|edu|net)')

matches = pattern.finditer(emails)







# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# matches = pattern.finditer(emails)

for match in matches:
    print(match)

