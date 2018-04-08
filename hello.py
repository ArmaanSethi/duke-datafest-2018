import pickle
import numpy as numpy
import matplotlib.pyplot as plt
import re
import csv

dates = pickle.load( open( "dates.p", "rb"))
duration = pickle.load( open( "duration.p", "rb"))
dbc = pickle.load( open("days_between_clicks.p", "rb"))
experience = pickle.load( open("experience.p", "rb"))
count = 0


for d in duration.keys():
	count = count + 1
	plt.scatter(int(re.search(r'\d+', str(duration[d])).group()), experience[d])
	if count ==1000:
		print("reach 1k")
		break
plt.show()