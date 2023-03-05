import email.utils
import re

for _ in range(int(input())):
    parser = email.utils.parseaddr(input())
    email_pattern = r"^[a-z][\w\-.]*@[a-z]+\.[a-z]{1,3}$"
    match = re.search(email_pattern, parser[1], re.I)
    if match:
        print(email.utils.formataddr(parser))
