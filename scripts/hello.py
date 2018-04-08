import pickle
import numpy as numpy
import matplotlib.pyplot as plt
import re
import csv
import datetime

#dates = pickle.load( open( "dates.p", "rb"))
#duration = pickle.load( open( "duration.p", "rb"))
#dbc = pickle.load( open("days_between_clicks.p", "rb"))
experience = pickle.load( open("experience.p", "rb"))
salary = pickle.load( open("salary.p", "rb"))
#companyRating = pickle.load( open("companyRating.p", "rb"))
wordCount = pickle.load( open("wordCount.p", "rb"))
jobAgeCount = pickle.load( open("jobage.p", "rb"))
clicks = pickle.load( open("clicks.p", "rb"))
#hoc = pickle.load( open("hoc.p", "rb"))
#category = pickle.load( open("category.p", "rb"))
count = 0
#cats = ['STEM', 'Business','Little/No Education', 'Liberal Arts', 'Technical', 'uncategorized']
# print(len(duration))
# print(len(companyRating))
#print(hoc.keys())
#print(hoc.values())
for d in clicks.keys():
	count = count + 1
	if jobAgeCount[d] != 0:
		plt.scatter(experience[d], clicks[d]/jobAgeCount[d])

	#int(re.search(r'\d+', str(d)).group())
	if count == 10000:
		print("reach 1k")
		break
	if count%1000 == 0:
		print("reach " + str(count/1000) + "k")
plt.show()