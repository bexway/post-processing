from __future__ import division
import Tkinter as tk
import tkFileDialog
from os import listdir
from os.path import isfile, join
import csv

class dataManager():
	def __init__(self, directory):
		self.data = []
		#Getting all the filenames from the directory
		self.directory = directory
		tempfiles = [f for f in listdir(self.directory) if isfile(join(directory, f))]
		self.files = []
		for f in tempfiles:
			if f[-4:] == ".csv":
				self.files += [f]
			else:
				print "File " + f + " isn't a csv! It wasn't included."

		for path in self.files:
			tempfile = 	open(directory + "/" + path, 'rb')
			reader = csv.DictReader(tempfile)
			headers = reader.fieldnames
			for row in reader:
				self.data += [row]
			tempfile.close()

		return

	def display_directory(self):
		print "The current directory path is: "
		print self.directory
		choice = raw_input("Would you like to change it? y/[n]: ")
		if choice == "y":
			print "Directory changing not implemented yet!"
			return
		else:
			return

	def display_files(self):
		print: "The files that have been read are:"
		for f in self.files:
			print f
		return
