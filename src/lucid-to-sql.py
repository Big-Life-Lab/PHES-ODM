'''
This script allows transforming the https://lucid.app/lucidchart - generated SQL 
code into a version that contains first the list of CREATE TABLE commands, followed 
by ALTER TABLE commands generated from CONSTRAINT, FOREIGN KEY and REFERENCES 
previously included in the CREATE TABLE commands.

This is necessary because the CREATE TABLE commands in the SQL code are generated
by Lucid in a order that doesn't follow the dependencies between tables,
so in its original form is not directly executable (because a CREATE TABLE at the
begining of the chain could have a constraint on a table that doesn't exist yet).

To get the SQL code from Lucid, click on the Export button under the Shapes left panel. 
In the pop-up window that appears, you have the option to select the SQL dialectand in
the frame below you get the generated SQL code.

If 'clip' variable equals 1, the script expects the SQL code copied in the clipboard 
(with Ctrl-C) and will replace the content of the clipboard with the modified form 
(CREATE TABLLE commands followed by ALTER TABLE commands) so you can paste it (with
Ctrl-V) in your database's query interface for execution.
If 'clip' variable is any other integer, like 0, the script expects a text file with
the SQL code as input and will (over)write the modified SQL code to the same, or other file.
'''

import os
from os.path import join, normpath
import re

current_dir = normpath(os.path.dirname(__file__))
root_dir = normpath(os.path.dirname(current_dir))

clip = 0 # 1 to process the clipboard, any other integer to process a file
start_sql_file = 'lucid-mysql.sql' # sql file that was exported from Lucid Chart
start_sql_path = join(current_dir, start_sql_file) # if starting directory is the same as the script direcotry).
output_file_folder = 'templates'
output_sql_file = 'ODM-mysql.sql'

# output file info
output_sql_dir = join(root_dir, output_file_folder)
output_sql_path = join(output_sql_dir,output_sql_file)

create = ''
alter = ''
table = ''
creFlag = False
altFlag = False
if clip == 1: 
    import pyperclip # make sure you have installed pyperclip with 'pip install pyperclip' in advance
    script = pyperclip.paste() # get the SQL script from the clipboard
else:
    with open(start_sql_path) as file: # make sure the path to the input file is correct
        script = file.read() # read the whole file
for line in script.split('\n'): # parse all the lines of the SQL script
    # set the altFlag to True if the line is not part of the table columns definition, but is part of the table altering commands (is containg the CONSTRAINT, FOREIGN KEY or REFERENCES keywords)
    altFlag = re.search('\s?CONSTRAINT\s',line,re.IGNORECASE) or re.search('\s?FOREIGN KEY\s',line,re.IGNORECASE) or re.search('\s?REFERENCES\s',line,re.IGNORECASE)
    # check if the line contains the CREATE TABLE command
    m = re.match('(.*CREATE TABLE )([\["`]?[^\]"`]*[\]"`]?)(.*)',line,re.IGNORECASE) 
    if m != None: # if the line contains a CREATE TABLE definition...
        table = m[2] # ...get the table name...
        creFlag = True # ...and set the creFlag to True for the following lines
        altFlag = False # if it's a CREATE TABLE line in Lucid, it can't be an ALTER TABLE line as well, so set the altFlag to False
    if creFlag and altFlag: # if previous lines were part of the table creation but current line is altering the table...
        create = create.strip() # store in the 'create' variable the table creation commands...
        if create[-1] == ',':
            create = create[0:len(create)-1]
        alter = alter + ';\nALTER TABLE ' + table + ' ADD \n' #...and in the 'alter' variable the table alteration commands
        creFlag = False # and set the creFlag to false, since this is a table altering, not table creation line
    if not creFlag and not altFlag: # but if a line is not of the table creation type and not of table altering type...
        creFlag = True # ...set it by default to be of table creation type
    if creFlag: # add the line to the 'create' variable
        create = create + line + '\n'
    if altFlag: # add the line to the 'alter' variable
        alter = alter + line + '\n'
if clip == 1:
    pyperclip.copy(create+alter+';') # replace the content of the clipboard with the create/alter commands in the proper order 
else:
    with open(output_sql_path,'w') as file: # make sure the path to the output file is correct. The file will be overwritten if it exists
        file.write(create+alter+';') # replace the content of the file with the create/alter commands in the proper order 
# print(create+alter)