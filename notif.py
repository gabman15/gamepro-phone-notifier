from notify_run import Notify 
import os
notify = Notify()

filename = "output.txt"
found = False
resetting = False
lastTwoLines = ""
i = 0

while not found:
	file = open(filename, "r")
	i = 0
	os.system('cls')
	for line in file:
		if "Shiny" in line:
			found = True
		else:
			i = i + 1
		if "Reset" in line:
			resetting = True
		if not resetting:
			print (line)
	file.close()
	if resetting:
		file = open(filename, "r")
		lines = file.readlines()
		print (lines[i-2] + lines[i-1])
	

file = open(filename, "r")
lines = file.readlines()

notify.send('Shiny found!!! Last lines:\n' + lines[i-3] + lines[i-2] + lines[i-1] + lines[i])