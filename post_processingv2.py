import Tkinter as tk
import tkFileDialog
from os import listdir
from os.path import isfile, join
import csv

# root = tk.Tk()
# root.withdraw()
# try directory = tkFileDialog.askopenfilename()

directory = "data"
onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

# parametersfile = open('eventsparameters.csv', 'r')
# parametersreader = csv.DictReader(parametersfile)
# responsefile = open('eventsresponses.csv', 'wb')
# responsefields = ['Response', 'RT']
# responsewriter = csv.DictWriter(responsefile, responsefields)
# responsewriter.writeheader()

datarows = [[], []]
surveyrows=[]
for path in onlyfiles:
	tempfile = 	open(directory + "/" + path, 'rb')
	reader = csv.DictReader(tempfile)
	headers = reader.fieldnames
	for row in reader:
		if "survey" in row["trial_type"]:
			# if "likert" in row["trial_type"]:
			# 	if "item" == row["Type"]:
			# 		datarows[0].append(row)
			# 	else:
			# 		datarows[1].append(row)
			# elif "text" in row["trial_type"]:
			surveyrows.append(row)
		elif "single" in row["trial_type"]:
			if "item" == row["Type"]:
				datarows[0].append(row)
			else:
				datarows[1].append(row)

	tempfile.close()

aggfile = open("Results/totaldata.csv", 'wb')
datafile = open("Results/targetAndFillerData.csv", 'wb')
targetfile = open("Results/targetData.csv", 'wb')
fillerfile = open("Results/fillerData.csv", 'wb')
surveyfile = open("Results/surveyData.csv", 'wb')

genfields = ["subject", "trial_index", "trial_type", "list"]
surveyfields = genfields + ["responses"]
datafields = ["Type", "Sentence", "Response"]
fillerfields = genfields + datafields + ["Fill1", "Fill2"]
targetfields = genfields + datafields + ["item", "cond", "repeatability", "IlluBare", "quantifier", "ellipsis", "additive"]
aggfields = surveyfields + targetfields + ["Fill1", "Fill2"]
datafields = targetfields + ["Fill1", "Fill2"]

aggwriter = csv.DictWriter(aggfile, aggfields)
aggwriter.writeheader()
surveywriter = csv.DictWriter(surveyfile, surveyfields)
surveywriter.writeheader()
datawriter = csv.DictWriter(datafile, datafields)
datawriter.writeheader()
targetwriter = csv.DictWriter(targetfile, targetfields)
targetwriter.writeheader()
fillerwriter = csv.DictWriter(fillerfile, fillerfields)
fillerwriter.writeheader()

for row in surveyrows:
	rowDict = {col: row[col] for col in surveyfields}
	surveywriter.writerow(rowDict)
	aggwriter.writerow(rowDict)
for row in datarows[0]:
	rowDict = {col: row[col] for col in targetfields}
	datawriter.writerow(rowDict)
	targetwriter.writerow(rowDict)
	aggwriter.writerow(rowDict)
for row in datarows[1]:
	rowDict = {col: row[col] for col in fillerfields}
	datawriter.writerow(rowDict)
	fillerwriter.writerow(rowDict)
	aggwriter.writerow(rowDict)

aggfile.close()
datafile.close()
targetfile.close()
fillerfile.close()
surveyfile.close()

#Goals: Remove view_history column, remove trial types not containing "survey", 
#Separate by trial types, separate by type column


