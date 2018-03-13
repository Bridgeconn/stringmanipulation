import csv
import pandas as pd

with open('copy.csv','r+',encoding='utf-8') as file:
    creader=csv.reader(file)
    cwriter=csv.writer(file)
    name=[]
    for row in creader:
        name+=row
    print(name)
    name.pop(0)
    name.insert(0,"Copied name")
    data = {name}
    print(data)
    df = pd.DataFrame(data)
    print(df)
    for word in df:
        cwriter.writerow([word])
    print (df)