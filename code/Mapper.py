#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    i = line[4]
    signs = i.count('.') + i.count('!') + i.count('?')
    if (signs == 0 or (signs == 1 and (i[-1] == '.' or i[-1] == '!' or i[-1] == '?'))):
        writer.writerow(line)
