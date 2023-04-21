# Extract SSns from text with regex
#print(re.findall(r'\d\d\d[- ]?\d\d[- ]?\d\d\d', x))
#print(re.findall(r'(\d{3}) [- ]?(\d{2}) [- ]?(\d{4})', x))
#print(list(map("-".join,(re.findall(r'(\d{3}) [- ]?(\d{2}) [- ]?(\d{4})', x)))))

import re
x = 'FK rCXlQFbzBi-ycD639 88 0024mSnqE rXNy-DT fCeuNiS396 57 3329TluZRkN-BQjiTsGsmjoDpHoMIwRKPpbfHJ882 61 9767cOFHfAXSR--nDTS-UwzEBxRsm652 95 6590NZ -lTzJRAnJaqouYDpsrW079 13 7369Q BOW-bCWS  rH-X VhlDYN -ZMJb817 72 5478uzWGfkGYMXIkVQeMsPApT001 26 9198sbAoL m dpqVCBIMd'



def findSSN(x):
    return list(map("-".join,(re.findall(r'(\d{3}) [- ]?(\d{2}) [- ]?(\d{4})', x))))

print(findSSN(x))