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