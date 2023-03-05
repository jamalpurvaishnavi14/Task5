import re

pattern = re.compile(r'#([0-9a-fA-F]{1,2}){3}')

res = []
for _ in range(int(input())):
    s = input()
    if s.endswith(';'):
        res += [m.group(0) for m in re.finditer(pattern, s)]
print(*res, sep='\n')
