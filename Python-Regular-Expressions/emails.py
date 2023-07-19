"""
Example:
Write a regular expression that will match different emails.
-character sets and quantifiers
-groups matching several different patterns
"""
import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
pattern = re.compile(r'[\w.-]+@[\w-]+\.(com|edu|net)') # another option

matches = pattern.finditer(emails)

for match in matches:
    print(match)
