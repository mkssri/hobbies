#!/usr/bin/python3

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# sentence = 'Start a sentence and then bring it to an end start'
sentence = 'murali Start a sentence and then bring it to an end start'


pattern = re.compile(r'start', re.I)

# matches = pattern.search(sentence)
matches = pattern.findall(sentence)
# matches = pattern.finditer(sentence)

# matches = pattern.match(sentence) # it cares about only start

# match and search gives first instance only



print(matches)

# for match in matches:
#     print(match.start())
#     print(match.end())
#     print("sentence - {}".format(sentence[match.start():match.end()]))
#     print(match.span())
#     print("Murali - {}".format(match.group()))
#     break


