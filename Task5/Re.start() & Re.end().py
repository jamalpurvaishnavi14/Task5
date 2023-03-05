import re

n = input()
m = input()
temp_set = set()
for i in range(0,len(n)):
    ans = re.search(rf"{m}",n) #To search and extract the start and end point of the regular expression
    if ans:
        temp_set.add((ans.start(),ans.end() - 1)) #Adding the (start, end) value to the set
        n = ("*"* (i+1)) + n[i+1:] # After updating changing the ith value of input string to "*"

temp_set = sorted(temp_set,key= lambda i :i[1]) #Sort the set 
if temp_set:
    for i in temp_set:
        print(i)
else:
    print("(-1, -1)")
