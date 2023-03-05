import re
trans = {'||': 'or', '&&': 'and'}
for _ in range(int(input())):
    print(re.sub('(?!^)(?<= )(\|\||&&)(?= )', lambda m: trans[m.group(1)], input()))
