from bs4 import BeautifulSoup
import re
import csv
import sys
import glob
import errno
import os

files = glob.glob('**/*.htm')
for name in files:
    file_name = os.path.splitext(name)[0]
    csv_file = file_name + '.csv'
    print csv_file

    soup = BeautifulSoup(open(name), "lxml")

    outfile = open(csv_file, 'w')

    # Create the csv writer object
    csvwriter = csv.DictWriter(outfile, fieldnames = ["Book Name", "Chapter", "Verse", "Strong Number", "Hebrew Eng", "Hebrew", "Eng Word", "Word Type"], delimiter ='\t')
    csvwriter.writeheader()
    a = ""
    verse = ""
    c = ""
    d = ""
    e = ""
    strong_num = ""
    strong_n = ""

    # Open html and obtain the table as input
    csvwriter = csv.writer(outfile, delimiter ='\t')
    table = soup.find_all("table", attrs={"class":"tablefloatheb"})
    print "Parsing HTML file"

    # Parse the table in html row by row
    book = (soup.find('div', id = "topheading")).get_text().encode('utf-8')
    book_name = (re.search('\d? [a-z]+', book, re.IGNORECASE)).group()
    chapter_no = file_name.split('/')[1]

    for t in table:
        for row in t.find_all("tr"):
            strong_num = ""
            for item in row.find_all('span', class_= 'eng'):
                a = item.get_text().encode('utf-8')
            for item in row.find_all('span', class_= 'refheb'):
                verse = item.get_text().encode('utf-8')
            for item in row.find_all('span', class_= 'strongsnt'):
                c = item.get_text().encode('utf-8')
            for item in row.find_all('span', class_= 'hebrew'):
                d = item.get_text().encode('utf-8')
            for item in row.find_all('span', class_= 'translit'):
                e = item.get_text().encode('utf-8')
            for item in row.find_all('span', class_= 'strongs'):
                if item != "":
                    strong_num = strong_num + item.get_text().encode('utf-8')

            p = re.compile('\d+\[e]')
            m = p.search(strong_num)
            if m:
                strong_n = m.group()
            else:
                strong_n = ""

            verse_no = (re.search(r'\d+', verse)).group()

            if strong_num != "":
                # Write to csv file 
                csvwriter.writerow([book_name, chapter_no, verse_no, strong_n, e, d, a, c])

    print "Converted to CSV !"
    outfile.close()
