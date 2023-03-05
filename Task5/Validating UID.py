import re

def is_valid_uid(uid):
    return all([
        re.search(r'[A-Z].*[A-Z]', uid),
        re.search(r'\d.*\d.*\d', uid),
        not re.search(r'\W', uid),
        len(set(uid)) == 10,
        len(uid) == 10
    ])

t = int(input().strip())

for i in range(t):
    uid = input().strip()
    if is_valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")
