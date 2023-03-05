regex_pattern = r"[\b\W\b]+"    # Do not delete 'r'.


import re
print("\n".join(re.split(regex_pattern, input())))
