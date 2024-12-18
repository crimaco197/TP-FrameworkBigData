#!/usr/bin/python
import csv
import sys

a = []
b = []

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line[4]) == 0:
        continue
    else:
        a.append(line)

# Sort by the longest body
sort_a = sorted(a, key=lambda a: len(a[4]), reverse=True)

# Take 10 first longest body
for i in range (0, 10):
    b.append(sort_a[i])

print("Voila les 10 posts les plus longes !")
for bl in b:
    # writer.writerow(bl)
    print(bl)
