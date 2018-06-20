'''
 Make three column in a .xlsx file and copy the third column in .txt file.
'''

import pandas as pd

data = pd.read_excel('data.xlsx')

''' Reading the perticular column by the name of column'''
data_col = data["Profession"]

''' Writing the content to the text file'''
data_col.to_csv('copied_content.txt', index=False, sep = ' ', header = True)