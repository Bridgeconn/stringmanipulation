import csv
import re
import sys
import glob
import errno
import os

files = glob.glob('**/*.usfm')
for name in files:
    file_name = os.path.splitext(name)[0]
    usfm_file = file_name[0:-3] + '.usfm'
    print usfm_file
    # open usfm file for reading
    infile = open (name,'r')

    # open csv file for writing
    outfile = open(usfm_file, 'w')

    d = infile.readlines()
    infile.seek(0)
    for line in d:
        newline = re.sub(r'(\\add)', '', line)
        outfile.write(newline)
    print "USFM errors removed !"

    # close the usfm and csv file
    infile.close()
    outfile.close()
