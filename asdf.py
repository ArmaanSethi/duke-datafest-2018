import csv
import pickle
from tqdm import tqdm

hoc = {}

with open('categories-Sheet1-1.csv', encoding = "utf8") as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in tqdm(enumerate(csvReader)):
		bigc = row[1]
		hoc[bigc[0]] = bigc[1]

pickle.dump(hoc, open("hoc.p", "wb"))
