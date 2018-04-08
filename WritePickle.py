import csv
import pickle
from tqdm import tqdm

# experienceRequired = {} 
# salaryArray = {}
# companyRating = {}
clicks = {}
jobage = {}
with open('datafest2018.csv', encoding = "utf8") as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for idx,row in tqdm(enumerate(csvReader)):
		if(idx < 1):
			print(row)
		else:
			country = row[3]
			jobID = row[2]
			companyID = row[1]
			click = int(row[21])
			age = int(row[20])
			if (country == 'US'):
				if jobID in clicks:
					if jobage[jobID] < age:
						jobage[jobID] = age
					clicks[jobID] += click
				else:
					clicks[jobID] = click
					jobage[jobID] = age


pickle.dump(clicks, open("clicks.p", "wb"))
pickle.dump(jobage, open("jobage.p", "wb"))





