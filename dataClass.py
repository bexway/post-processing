from __future__ import division
import Tkinter as tk
import tkFileDialog
from os import listdir
from os.path import isfile, join
import csv

class dataManager():
	readers = {}
	writers = {}

	def __init__(self, directory):
		self.directory = directory
		tempfiles = [f for f in listdir(self.directory) if isfile(join(directory, f))]
		self.files = []
		for f in tempfiles:
			if f[-4:] == ".csv":
				self.files = self.files + [f]
			else:
				print "File " + f + " isn't a csv! It wasn't included."


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
