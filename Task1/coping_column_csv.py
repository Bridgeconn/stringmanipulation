# CSV file, add data in one column with heading "Name" 
# and copy this created column in new column with heading "Copied name"


import csv
import pandas as pd

with open('copy.csv', 'r+', encoding = 'utf-8') as file:
	data = pd.read_csv("copy.csv", sep = ',')
	creader = csv.reader(file)
	cwriter = csv.writer(file)

	for name in creader:
		#Updating the column name
		data["Copied Name"] = data["Name"]
		data.to_csv("copy.csv", index = False)