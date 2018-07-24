import sys
import math
from collections import OrderedDict

def main(argv):
	processInput(argv[0])
	

def processInput(input_file):
	fin = open(input_file, "r")
	fin2 = open(input_file, "r")
	fin3 = open(input_file, "r")
	fin4 = open(input_file, "r")
	

	constraintDict = {}

	users = []
	birds = []
	#"Reduced" because we are reducing, for any given Bird, their entire ride history throughout
	# the simulation to one pair of start and stop locations: their first start ("DROP") and their last stop.
	reducedTrips = []
	trips = []

	for i in range(220):
		constraint = fin.readline().split(",")

		c = constraint
		m = [k for v,k in enumerate(constraint)]
		constraintDict[i] = c
		timestamp = int(str(m[0]))
		bird_id = str(m[1])
		event_type = str(m[2])
		x = float(str(m[3]))
		y = float(str(m[4]))
		user_id = str(m[5])

		if i == 222:
			print(timestamp+", "+bird_id+", "+event_type+", "+x+", "+y+", "+user_id)

		if user_id not in users:
			users.append(user_id)
		if event_type == 'DROP':
			reducedTrips.append((bird_id,x,y,x,y,timestamp,0))
			trips.append((bird_id,True,x,y,x,y,timestamp,0))
			birds.append(bird_id)
		#if event_type == 'START_RIDE':

	for i2 in range(220):
			constraint = fin2.readline().split(",")

			c = constraint
			m = [k for v,k in enumerate(constraint)]

			constraintDict[i2] = c
			timestamp = int(str(m[0]))
			bird_id = str(m[1])
			event_type = str(m[2])
			x = float(str(m[3]))
			y = float(str(m[4]))
			user_id = str(m[5])			
			#if event_type == 'END_RIDE':
			#print('bingo!')
			j=0
			tempCopy = reducedTrips
			for index,tupleV in enumerate(reducedTrips):
				if tupleV[0] == bird_id:
					#print('bingo!')
					if int(tupleV[5]) < int(timestamp):
						lst = list(tupleV)
						lst[3] = x
						lst[4] = y
						t = tuple(lst)
						reducedTrips[index]=t
				#reducedTrips = tempCopy
				j=j+1
	jk=0
	for tupleVI in reducedTrips:
		tempCopy2 = reducedTrips
		lst = list(tupleVI)
		#print(str(tupleVI[1])+", "+str(tupleVI[2])+", "+str(tupleVI[3])+", "+str(tupleVI[4]))
		subOp1 = (tupleVI[1]-tupleVI[3])**2
		subOp2 = (tupleVI[2]-tupleVI[4])**2
		lst[6] = math.sqrt(subOp2+subOp1)
		#(((float(tupleVI[1])-(float(tupleVI[3]))**2)*math.sin(math.radians(float(tupleVI[3])))+math.cos(math.radians(float(tupleVI[1]))))#*math.cos(math.radians(float(tupleVI[3])))*math.cos(math.radians(float(tupleVI[4]))-math.radians(float(tupleVI[2]))))*6371
		t = tuple(lst)
		reducedTrips[jk]=t
		#reducedTrips = tempCopy2
		jk=jk+1
	numOfBirds = len(birds)
	print("The total number of Bird vehicles dropped off in the simulation is "+str(len(birds))+".")
	maxP = 0
	for index,tupleV in enumerate(reducedTrips):
		if maxP < tupleV[6]:
			maxP = tupleV[6]
			b_id = tupleV[0]
	print("The Bird that ends up farthest away from its drop location is "+b_id+" with a distance of "+str(maxP)+".")
	for i3 in range(220):
			constraint = fin3.readline().split(",")

			c = constraint
			m = [k for v,k in enumerate(constraint)]

			constraintDict[i3] = c
			timestamp = int(str(m[0]))
			bird_id = str(m[1])
			event_type = str(m[2])
			x = float(str(m[3]))
			y = float(str(m[4]))
			user_id = str(m[5])	
			if event_type == 'END_RIDE':
				for index,tupleV in enumerate(trips):
					if tupleV[0] == bird_id:
						if tupleV[2] == False:
							#print('bingo!')
							lst = list(tupleV)
							lst[4] = x
							lst[5] = y
							lst[2] = False
							lst[6] = timestamp
							t = tuple(lst)
							trips[index]=t
	jkl=0
	for tupleVI in trips:
		lst = list(tupleVI)
		#print(str(tupleVI[1])+", "+str(tupleVI[2])+", "+str(tupleVI[3])+", "+str(tupleVI[4]))
		subOp1 = (tupleVI[1]-tupleVI[3])**2
		subOp2 = (tupleVI[2]-tupleVI[4])**2
		lst[6] = math.sqrt(subOp2+subOp1)
		#(((float(tupleVI[1])-(float(tupleVI[3]))**2)*math.sin(math.radians(float(tupleVI[3])))+math.cos(math.radians(float(tupleVI[1]))))#*math.cos(math.radians(float(tupleVI[3])))*math.cos(math.radians(float(tupleVI[4]))-math.radians(float(tupleVI[2]))))*6371
		t = tuple(lst)
		trips[jkl]=t
		#reducedTrips = tempCopy2
		jkl=jkl+1
	for i3 in range(220):
			constraint = fin4.readline().split(",")

			c = constraint
			m = [k for v,k in enumerate(constraint)]

			constraintDict[i3] = c
			timestamp = int(str(m[0]))
			bird_id = str(m[1])
			event_type = str(m[2])
			x = float(str(m[3]))
			y = float(str(m[4]))
			user_id = str(m[5])	
			if event_type == 'END_RIDE':
				if int(tupleV[6]) < int(timestamp):
					for index,tupleV in enumerate(trips):
						if tupleV[0] == bird_id:
							aDsupOp1 = (x-tupleV[4])**2
							aDsupOp2 = (y-tupleV[5])**2
							addedDistance = math.sqrt(aDsupOp2+aDsupOp1)
							updatedDistance = tupleV[6] + addedDistance
							lst = list(tupleV)
							lst[4] = x
							lst[5] = y
							lst[6] = timestamp
							lst[7] = updatedDistance
							t = tuple(lst)
							trips[index]=t
	for index,tupleV in enumerate(reducedTrips):
		if maxP < tupleV[7]:
			maxP = tupleV[6]
			b_id = tupleV[0]


	

if __name__ == '__main__':
	main(sys.argv[1:])