# A first Python script

###########################
# Importing a whole modie #
###########################

import sys                  # Load a library module
print(sys.platform)
print(sys.platform, sys.version)

##########################################
# Importing a single field from a module #
##########################################

from sys import platform, version
print(platform, version)

##############################
# Check contents of a module #
##############################

print("before dir")
print(dir(sys))
print("after  dir")

####################
# Change directory #
####################

print("Before os.listdir")
#exit(0)
import os
os.chdir(r"C:\Users\16028\PycharmProjects\spearson8872")
TheseFiles = os.listdir(r"C:\Users\16028\PycharmProjects\spearson8872")
print(TheseFiles)
print(TheseFiles[2])
for TheseNames in TheseFiles:
	print(TheseNames)
print( "After os.listdir")

exec(open('Second.py').read())

print( "After Second.py")

########################
# Read from one file   #
# and write to another #
########################

InFile=open('datain.txt', 'r')
# OutFile=open('dataout.txt', 'w')
OutFile=open('dataout.txt', 'a')
oneline=InFile.readline()
OutFile.write(oneline)

print('Before Close - Press Enter to exit') # was input

InFile.close()
OutFile.close()
print('After Close - Press Enter to exit') # was input

print (oneline)

print('After display - Press Enter to exit') # was input

#################################
# read whole file into an array #
#################################

print('Before open2 - Press Enter to exit') # was input

InFile=open('datain.txt', 'r')

print('Before full file read - Press Enter to exit') # was input

alllines=InFile.readlines()

print('Before full file display - Press Enter to exit') # was input

print(alllines)

print('Before full file sorted display - Press Enter to exit') # was input
print(type(alllines))
sortedlines=alllines
alllines.sort()
print(type(sortedlines))
print(sortedlines)
print("single item")
single_field = sortedlines[2]
print(single_field)

sortedlines=sorted(alllines)

print('Before Close - Press Enter to exit') # was input
InFile.close()
print('After Close - Press Enter to exit') # was input

########
# Math #
########

print(2 ** 100)             # Raise 2 to a power
x = 'Spam!'
print(x * 8)                # String repetition

####################################
# Conditionals and loops are       #
# delimited by change in embedding #
####################################

for x in 'test':
  print (x)
print('xx')

####################################
# Trick for windows. make this the #
# last line of a script and it can #
# by run from file explorer        #
####################################

print('Press Enter to exit') # was input