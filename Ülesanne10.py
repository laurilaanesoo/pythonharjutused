#Ülesanne10
#02.03.2022
#Lauri Laanesoo

import re

fh = open('nimekiri.txt')
for line in fh:
    if re.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', line):  
        print(line,end='')
    
fh = open('nimekiri.txt')
for rida in fh:
    if re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])", rida):
        print(rida,end='')
