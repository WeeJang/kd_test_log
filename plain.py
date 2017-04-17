import sys

print "[",
for line in sys.stdin.readlines():
	line = line.strip()
	print 1.0 * float(line),",",


print "]",
