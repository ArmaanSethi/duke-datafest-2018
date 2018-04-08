import csv
import pickle
from tqdm import tqdm

# experienceRequired = {} 
# salaryArray = {}
# companyRating = {}
wordCount = {}
with open('datafest2018.csv', encoding = "utf8") as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for idx,row in tqdm(enumerate(csvReader)):
		if(idx < 1):
			print(row)
		else:
			country = row[3]
			jobID = row[2]
			companyID = row[1]
			# experience = row[13]
			# if experience == "":
			# 	experience = 0
			# #print(experience)
			# if(country == 'US'):
			# 	if jobID in experienceRequired:
			# 		if experienceRequired[jobID] == 0:
			# 			experienceRequired[jobID] = experience
			# 	else: 
			# 		experienceRequired[jobID] = experience

			# salary = row[14]
			# if (country == 'US'):
			# 	if jobID in salaryArray:
			# 		if salary > salaryArray[jobID]:
			# 			salaryArray[jobID] = salary
			# 	else:
			# 		salaryArray[jobID] = salary

			# cRating = row[6]
			# if cRating == "":
			# 	cRating = 0;
			# if (country == 'US'):
			# 	if float(cRating) > -0.1:
			# 		if jobID in companyRating:
			# 			if cRating > companyRating[jobID]:
			# 				companyRating[jobID] = cRating
			# 		else:
			# 			companyRating[jobID] = cRating

			words = row[12]
			if (country == 'US'):
				if jobID in wordCount:
					if words > wordCount[jobID]:
						wordCount[jobID] = words
				else:
					wordCount[jobID] = words



# pickle.dump(experienceRequired, open("experience.p", "wb"))
# pickle.dump(salaryArray, open("salary.p", "wb"))
# pickle.dump(companyRating, open("companyRating.p", "wb"))
pickle.dump(wordCount, open("wordCount.p", "wb"))





