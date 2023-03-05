import re

for i in range(int(input())):
    
    text = input()
    pattern = re.compile(r"^([456][\d+]{3})-([\d+]{4})-([\d+]{4})-([\d+]{4})$|^([456][\d+]{15})$")

    if pattern.match(text):
        text = ''.join([i for i in text if i != '-'])
        if all([False if i*4 in text  else True for i in set(text)]):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")   
