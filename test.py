import re

pattern = '\d{3}/\w{3}'
pattern = '(?P<id>\d{3})/(?P<name>\w{3})'
string = 'weeew34ttt123/aaa'
ret = re.search(pattern, string)
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))
