import re
mobile_number = []
for _ in range(0,int(input())):
    mobile_number.append(input())
for i in mobile_number:
    if len(i)==10:
        if re.search('[789][0-9]{9}',i):
            print("YES")
        else:
            print("NO")
    else:
            print("NO")
