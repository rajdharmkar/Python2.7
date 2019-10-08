 set()={} # holds lines already seen
outfile = open("new2.txt", "w")#the text files have to be in same dir as py files
infile = open("new3.txt", "r")
print infile
print lines_seen
for line in infile:
        lines_seen = line
        print lines_seen
    #if line not in lines_seen: # not a duplicate
        outfile.write(line)
for line in open("new2.txt", "r"):
         print line
     #  lines_seen.add(line)
outfile.close()
