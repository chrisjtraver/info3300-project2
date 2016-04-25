import os
import pandas as pd
directory = "CSV_Stats/"
for filename in os.listdir(directory):
	df = pd.read_csv(directory + filename)

	for index, row in df.iterrows():
		if row['Season'][:2] == '19' or row['Season'][:2] != '20':
			continue
		else:
			df.drop(index, inplace=True)

	print(df)