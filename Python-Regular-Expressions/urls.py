import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls) # subtitute out matches with group 2 and 3 (back-refs)

print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))
