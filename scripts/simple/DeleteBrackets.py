#!/usr/bin/python3

# Read in the file
with open('MSSQLCreateTables.sql', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('[', '')
filedata = filedata.replace(']', '')

# Write the file out again
with open('SQLCreateTables.sql', 'w') as file:
  file.write(filedata)
