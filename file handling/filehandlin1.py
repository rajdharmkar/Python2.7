lines_seen = set()  # holds lines already seen
outfile = open('new2.txt', "w")
infile = open('new3.txt', "r")
# for line in open(new3.txt, "r"):
for line in infile:
    print line
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
for line in open(outfile, 'r'):
    print line
outfile.close()
print '--------------------------------------------------'
for line in open(lines_seen, 'r'):
    print line
