# This program opens file foo.txt and removes duplicate lines and writes the same to bar.txt file
lines_seen = set()  # holds lines already seen
outfile = open('foo.txt', "w")
infile = open('bar.txt', "r")
print "The file bar.txt is as follows"
for line in infile:
    print line

    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print "The file foo.txt is as follows"
for line in open('foo.txt', "r"):
    print line


