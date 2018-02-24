"""
9.4 Write a program to read through the mbox-short.txt and figure out who
has the sent the greatest number of mail messages. The program looks for
'From ' lines and takes the second word of those lines as the person who
sent the mail. The program creates a Python dictionary that maps the sender's
mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary
using a maximum loop to find the most prolific committer.
"""


handle = open("mbox-short.txt")
sender=dict()
bigcount = None
biganame = None

for line in handle :
    if line.startswith('From '):
        line=line.split()
        sender[line[1]] = sender.get(line[1],0) + 1

for name,count in sender.items() :
    if  count > bigcount :
        bigcount=count
        bigname = name

print (bigname,bigcount)
