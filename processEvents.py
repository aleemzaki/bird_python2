import sys
import math
from collections import OrderedDict

def main(argv):
	#print "Hello!"
	#if len(argv) != 96:
	#	print("Usage: python phase2algorithm.py [path_to_input#.py] [path_to_output#.py]")
	#	return#need to create .out beforehand
	#print "Hey!"
	#finalOrder = 
	processInput(argv[0])
	#print finalOrder

def processInput(input_file):
	fin = open(input_file, "r")
	fin2 = open(input_file, "r")
	

	constraintDict = {}

	users = []
	birds = []
	#"Reduced" because we are reducing, for any given Bird, their entire ride history throughout
	# the simulation to one pair of start and stop locations.
	reducedTrips = []

		#currentConstraint = []

	for i in range(220):
			constraint = fin.readline().split(",")

			c = constraint
			m = [k for v,k in enumerate(constraint)]

			constraintDict[i] = c
			timestamp = str(m[0])
			bird_id = str(m[1])
			event_type = str(m[2])
			x = str(m[3])
			y = str(m[4])
			user_id = str(m[5])

			if i == 222:
				print(timestamp+", "+bird_id+", "+event_type+", "+x+", "+y+", "+user_id)

			if user_id not in users:
				users.append(user_id)
			if event_type == 'DROP':
				reducedTrips.append((bird_id,x,y,x,y,timestamp,0))
				birds.append(bird_id)

	for i in range(220):
			constraint = fin2.readline().split(",")

			c = constraint
			m = [k for v,k in enumerate(constraint)]

			constraintDict[i] = c
			timestamp = str(m[0])
			bird_id = str(m[1])
			event_type = str(m[2])
			x = float(str(m[3]))
			y = float(str(m[4]))
			user_id = str(m[5])			
			if event_type == 'END_RIDE':
				#print('bingo!')
				j=0
				#tempCopy = reducedTrips
				for tupleV in reducedTrips:
					if tupleV[0] == 'JUVS':
						#print('bingo!')
						if int(tupleV[5]) < int(timestamp):
							lst = list(tupleV)
							lst[3] = x
							lst[4] = y
							t = tuple(lst)
							reducedTrips[j]=t
							#reducedTrips = tempCopy
	jk=0
	for tupleVI in reducedTrips:
		#tempCopy2 = reducedTrips
		lst = list(tupleVI)
		print(tupleVI[1])
		lst[6] = math.sqrt(((float(tupleVI[1])-float(tupleVI[3]))**2)-((float(tupleVI[2])-float(tupleVI[4]))**2))
		#(((float(tupleVI[1])-(float(tupleVI[3]))**2)*math.sin(math.radians(float(tupleVI[3])))+math.cos(math.radians(float(tupleVI[1]))))#*math.cos(math.radians(float(tupleVI[3])))*math.cos(math.radians(float(tupleVI[4]))-math.radians(float(tupleVI[2]))))*6371
		t = tuple(lst)
		reducedTrips[jk]=t
		#reducedTrips = tempCopy2
		jk=jk+1
	numOfBirds = len(birds)
	print("The total number of Bird vehicles dropped off in the simulation is "+str(len(birds))+".")
	print(reducedTrips)

if __name__ == '__main__':
	main(sys.argv[1:])