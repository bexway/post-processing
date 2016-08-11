from __future__ import division
import Tkinter as tk
import tkFileDialog
from os import listdir
from os.path import isfile, join
import csv

class dataManager():
	def __init__(self, directory):
		data = []
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
				data += [row]
			tempfile.close()

		self.archive = {"init_total_data":[data, headers]}
		self.active_data = self.archive["init_total_data"]

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
		print "The files that have been read are:"
		for f in self.files:
			print f
		return

	def clear_archive(self):
		data = self.archive["init_total_data"][0]
		headers = self.archive["init_total_data"][0]
		self.archive = {"init_total_data":[data, headers]}
		self.active_data = self.archive["init_total_data"]
		print "Archives cleared! All that's left is the initial archive of all files' data."
