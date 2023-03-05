import re

n, m = input().split()
n, m = int(n), int(m)

line_list = []
for i in range(n):
    line = input()
    line_list.append(line)

transposed_tuple_list = list(zip(*line_list))

joined_string = ''
for i in transposed_tuple_list:
    joined_string = joined_string + ''.join(i)
    
print(re.sub(r'(?<=[a-zA-Z0-9])[!@#$%&\s]+(?=[a-zA-Z0-9])', ' ', joined_string))
