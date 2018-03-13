import csv
import pandas as pd

with open('copy.csv','r+',encoding='utf-8') as file:
	df = pd.read_csv("copy.csv",sep=',')
	creader=csv.reader(file)
	cwriter=csv.writer(file)

	for name in creader:
		#print(name)
		df["Copied Name"] = df["Name"]
		df.to_csv("copy.csv",index=False)