'''Copy the ERD SQL from Lucid chart (the script should be fit for all but Quickbase SQL scripts, which are JSON-organized) then execute the script below the image, which processes the text in the clipboard. The script will separate the CREATEs from the required ALTERs for FKs and print them in the Python console, so you can copy the output of this script (the two print commands at the end of the script) and execute them in your database  to create the model.'''

import re
from tkinter import Tk
script = Tk().clipboard_get()
create = ''
alter = ''
table = ''
creFlag = False
altFlag = False
for line in script.split('\n'):
    #print(line)
    altFlag = re.search('\s?CONSTRAINT\s',line,re.IGNORECASE) or re.search('\s?FOREIGN KEY\s',line,re.IGNORECASE) or re.search('\s?REFERENCES\s',line,re.IGNORECASE)
    m = re.match('(.*CREATE TABLE )([\["`]?[^\]"`]*[\]"`]?)(.*)',line,re.IGNORECASE) 
    if m != None:
        table = m[2]
        #print(table)
        creFlag = True
        altFlag  =False
    if creFlag  and altFlag:
        create = create.strip()
        if create[-1] == ',':
            create = create[0:len(create)-1]
        alter = alter + ';\nALTER TABLE ' + table + ' ADD \n'
        creFlag = False
    if not creFlag  and not altFlag:
        creFlag = True
    if creFlag:
        create = create + line + '\n'
    if altFlag:
        alter = alter + line + '\n'
print(create)
print(alter)