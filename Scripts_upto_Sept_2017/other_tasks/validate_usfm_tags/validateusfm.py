import re

# Read the contents of the usfm file
filename = "3JN.usfm"
print "The file being read is: %r \n" % filename

txt = open(filename)

# Search for valid tags line by line
with open ('3JN.usfm','r') as txt:
    for line in txt:
        m = re.findall("\\\[a-z]{1,3}\d?", line)
        n = re.search("\\\[a-z]{1,3}\*", line)
        if m:
            if n:
                print n.group(0),
                print 'Character tags'
            print m,
            print ('Valid tag\n')
        else:
            if line == "\n":
                continue
            else:
                print ('Invalid tag\n')
