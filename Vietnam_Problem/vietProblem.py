#!/usr/bin/env python3

from multiprocessing import Pool
from multiprocessing import cpu_count

def solutions(permutationList):
	solutionsList= []
	#print(permutationList)
	for i in permutationList:
		var1 = i[0]
		var2 = i[1]
		var3 = i[2]
		var4 = i[3]
		var5 = i[4]
		var6 = i[5]
		var7 = i[6]
		var8 = i[7]
		var9 = i[8]

		solution = var1 + 13 * var2 / var3 + var4 +12 * var5 -var6 - 11 + var7 * var8 / var9 - 10
		if (solution == 66):
			solutionsList.append(i)
	return(solutionsList)

def permutateList(Array, value):	
	print(value)
	n = len(Array)
	c = []
	outputList = []
	i = 0

	while (i<n):
		c.append(0)
		i = i+1

	i=0
	if (Array[n-1] != value):
		temp = Array[n-1]
		Array[n-1] = Array[value-1]
		Array[value-1] = temp

	outputList.append(Array[:])
	while (i<n) and (Array[n-1] == value):
		if (c[i]<i):
			if (i%2 == 0):
				temp = Array[0]
				Array[0] = Array[i]
				Array[i] = temp
			else:
				temp = Array[c[i]]
				Array[c[i]] = Array[i]
				Array[i] = temp

			outputList.append(Array[:])
			c[i] = c[i]+1
			i = 0
		else:
			c[i] = 0
			i = i+1

	outputListFinal = solutions(outputList)
	return (outputListFinal)

"""def divideList(inputList, processCount):
	
	step = max(1, len(inputList)//processCount)

	#reduces number of processes if there are more than the number of inputValues
	processCount = min(processCount, len(inputList))

	#A list of lists of size len(inputList)/processCount
#	outputList = []
	number = 1

	while (number<processCount):
		beginning = number*step

		if (number<processCount-1):
			end = (number+1)

		else:
			end = len(inputList)
		
		outputList.append(inputList[beginning:end])
		number+=1

	return (outputList) """

def runAsync(inputList, lastValList, func, processCount):
	numIndices = len(inputList)
	index = 0
	#generates a list of permutations
	outputList = []
	#generates a list of processes created
	processList = []
	#creates a 'pool' of processes in which to grab from to run a function
	with Pool(processes = processCount) as pool:
		#starts processCount number of processes
		for lastVal in lastValList:
			value = lastVal
			#starts the processes so they can run independently of one another
			process = pool.apply_async(func, [inputList, value])
			#adds the process number to a list in which to .get from
			processList.append(process)
			
			print("Process ", index, " started.")
			index = index+1
		
		for number, process in enumerate(processList):
			#'gets' permutation in which to put in outputList[]
			outputValue = process.get()
			for l in outputValue:
				outputList.append(l)
		
			print("Process ", index, " finished.")
		
	return(outputList)

def main():
	numList = [1,2,3,4,5,6,7,8,9]
	processCount = cpu_count()
	#dividedNumList = (numList, processCount)
	lastValList = [9,6,5,4,3,2,7,8,1]
	outputList = runAsync(numList, lastValList, permutateList, processCount)
	numSolutions = 0
	#outputList = permutateList(numList, 9)
	for x in outputList:
		numSolutions = numSolutions+1
		print(x)

	print(numSolutions)
	"""for i in range(dividedNumList):
		for j in range(dividedNumList[i]):
			print(str(dividedNumList[i][j]))"""

if ( __name__ == "__main__" ):
	main()
