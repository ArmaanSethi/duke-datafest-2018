import csv
import pickle
from tqdm import tqdm

experienceRequired = {} 
with open('datafest2018.csv', encoding = "utf8") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for idx,row in tqdm(enumerate(csvReader)):
        if(idx < 1):
            print(row)
        else:
            country = row[3]
            jobID = row[2]
            companyID = row[1]
            experience = row[13]
            if experience == "":
            	experience = 0
            #print(experience)
            if(country == 'US'):
            	if jobID in experienceRequired:
            		if experienceRequired[jobID] == 0:
            			experienceRequired[jobID] = experience
            	else: 
            		experienceRequired[jobID] = experience

pickle.dump(experienceRequired, open("experience.p", "wb"))
