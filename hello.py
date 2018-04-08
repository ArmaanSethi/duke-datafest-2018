import pickle
import numpy as numpy
import matplotlib.pyplot as plt
import re
import csv
import datetime

dates = pickle.load( open( "dates.p", "rb"))
duration = pickle.load( open( "duration.p", "rb"))
dbc = pickle.load( open("days_between_clicks.p", "rb"))
experience = pickle.load( open("experience.p", "rb"))
# salary = pickle.load( open("salary.p", "rb"))
# companyRating = pickle.load( open("companyRating.p", "rb"))
# wordCount = pickle.load( open("wordCount.p", "rb"))
count = 0
# print(len(duration))
# print(len(companyRating))
for d in duration.keys():
# for d in companyRating.keys():
	if int(re.search(r'\d+', str(duration[d])).group()) < 99:
		count = count + 1
		plt.scatter(int(re.search(r'\d+', str(duration[d])).group()), experience[d])
		# plt.scatter(int(re.search(r'\d+', str(duration[d])).group()), salary[d])
		# plt.scatter(int(re.search(r'\d+', str(duration[d])).group()), companyRating[d])
		# plt.scatter(int(re.search(r'\d+', str(duration[d])).group()), wordCount[d])
		if count == 10000:
			print("reach 1k")
			break
		if count%1000 == 0:
			print("reach " + str(count/1000) + "k")
plt.show()