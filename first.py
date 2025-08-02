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

exit(0)
InFile=open('datain.txt', 'r')
# OutFile=open('dataout.txt', 'w')
OutFile=open('dataout.txt', 'a')
oneline=InFile.readline()
OutFile.write(oneline)

raw_input('Before Close - Press Enter to exit')
InFile.close()
OutFile.close()
raw_input('After Close - Press Enter to exit')

print (oneline)

raw_input('After display - Press Enter to exit')

#################################
# read whole file into an array #
#################################

raw_input('Before open2 - Press Enter to exit')

InFile=open('datain.txt', 'r')

raw_input('Before full file read - Press Enter to exit')

alllines=InFile.readlines()

raw_input('Before full file display - Press Enter to exit')

print(alllines)

raw_input('Before full file sorted display - Press Enter to exit')
print(type(alllines))
sortedlines=alllines
alllines.sort()
print(type(sortedlines))
print(sortedlines)
print("single item")
print(PyList_GetItem(sortedlines,2))

sortedlines=sorted(alllines)

raw_input('Before Close - Press Enter to exit')
InFile.close()
raw_input('After Close - Press Enter to exit')

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

raw_input('Press Enter to exit')