__author__ = 'Dyachkov'

# This is test email extractor.
# http://www.regular-expressions.info/email.html

import re

test = 'test $100 apples 333 times'
patt = r'(?<![$])\d{3}\s+\w+'

mtc = re.findall(patt, test)
print (mtc)

strings = ["name@namet@cs.name.edu", "test444.namez(at)cs.name.edu", "l@ombe@cs.name.edu"]

patt = r'(^[^@]*\w+)(@)(\w+)(\.name\.edu)'
patt = r'\b(?<!@)(\w+)(@)(\w+\.name.edu)'
patt = r"\b(?<!@)([a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*)(@|\(at\))(\w+\.name.edu)\b"

for line in strings:
    matches = re.findall(patt, line)
    email = ''
    for m in matches:
        for group in m:
            email += str(group).strip().replace('(at)', '@').replace('dot','.')
    print (email)

phone = r"(?<=([\(.]?))[0-9]\d\d(?=([\).]?))[ -]?[2-9]\d\d[-.]\d{4}"
line = "Phone: (650)814-1478 [Cell], Fax: (650)723-1614<o:p></o:p><br>"
line = "(650)8"
phone = "(?<=([\(.]))([0-9]\d\d)(?=([\).]?))\d"
matches = re.findall(phone, line)
for m in matches:
    print(m)