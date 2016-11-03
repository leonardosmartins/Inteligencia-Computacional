import time
import sys

def readFile(patchFile, fileName):
	file = open('../'+patchFile+'/'+fileName, 'r')
	body = file.read()
	file.close()
	inputFile = range(31) 
	inputFile[30] = 0

	for i in range(30):
		inputFile[i] = int (body[i*2])

	return inputFile
		
def createMatrix(lin, col):
	matrix = []
	for i in range(lin):
		matrix.append([0] * col)

	return matrix

def fillMatrix(size):
	for i in range(size):
		trainningMatrix[i] = readFile('Trainning-Input', str(i)+'.txt')

	return trainningMatrix	

def train(neuronio,weightMatrix, trainningMatrix):
	verifyInput = range(len(trainningMatrix))
	verifyEnd = 1
	epoch = 0

	while(verifyEnd != 0):
		epoch += 1
		for j in range(len(trainningMatrix)):
			result = 0
			for i in range(len(weightMatrix[0])):
				result = result + weightMatrix[neuronio][i] * trainningMatrix[j][i]

			if result > 0:
				result = 1
			else:
				result = 0		
	
			if result == 0 and j == neuronio:
				for i in range(len(weightMatrix[0])):
					weightMatrix[neuronio][i] = weightMatrix[neuronio][i] + trainningMatrix[j][i]

				verifyInput[j] = 1			

			elif result == 1 and j != neuronio:		
				for i in range(len(weightMatrix[0])):
					weightMatrix[neuronio][i] = weightMatrix[neuronio][i] - trainningMatrix[j][i]
				
				verifyInput[j] = 1			

			else:
				verifyInput[j] = 0

		verifyEnd = 0
		for i in range(len(verifyInput)):
			verifyEnd = verifyEnd + verifyInput[i] 					
	
	print "Neuronio",neuronio,"\nEpocas necessarias para treinar:",epoch, "\nVetor de pesos:",weightMatrix[neuronio],'\n\n'
	return weightMatrix			

def verifyNeuronio(weightMatrix, matrixInput, neuronio, inputName1, inputName2):
	result = 0
	for i in range(len(weightMatrix[0])):
		result = result + weightMatrix[neuronio][i] * matrixInput[i]

	if result > 0:
		result = 1
	else:
		result = 0

	print "Neuronio:",neuronio, "<==>", "Entrada:", inputName1, "-", inputName2, "<==>", "Resultado",result			

if int(sys.argv[1]) == 1:
	#EXERCISE 1
	weightMatrix = createMatrix(2,31)
	trainningMatrix = createMatrix(2,31)
	trainningMatrix = fillMatrix(2)
	matrixInput = range(31)

	for i in range(len(weightMatrix)):
		weightMatrix[i][30] = 1

	weightMatrix = train(1,weightMatrix,trainningMatrix)

	for i in range(6):
		print '\n'
		for j in range(10):
			matrixInput = readFile('Input', str(i)+'-'+str(j)+'.txt')
			verifyNeuronio(weightMatrix,matrixInput,1,i,j)

elif int(sys.argv[1]) == 2:
	#EXERCISE 2
	weightMatrix = createMatrix(2,31)
	trainningMatrix = createMatrix(2,31)
	trainningMatrix = fillMatrix(2)
	matrixInput = range(31)

	for i in range(len(weightMatrix)):
		weightMatrix[i][30] = 1

	weightMatrix = train(0,weightMatrix,trainningMatrix)
	weightMatrix = train(1,weightMatrix,trainningMatrix)

	for i in range(6):
		print '\n'
		for j in range(10):
			matrixInput = readFile('Input', str(i)+'-'+str(j)+'.txt')
			verifyNeuronio(weightMatrix,matrixInput,0,i,j)		
			verifyNeuronio(weightMatrix,matrixInput,1,i,j)

elif int(sys.argv[1]) == 3:
	#EXERCISE 3
	weightMatrix = createMatrix(6,31)
	trainningMatrix = createMatrix(6,31)
	trainningMatrix = fillMatrix(6)
	matrixInput = range(31)

	for i in range(len(weightMatrix)):
		weightMatrix[i][30] = 1

	for i in range(len(weightMatrix)):
		weightMatrix = train(i,weightMatrix,trainningMatrix)

	for i in range(len(weightMatrix)):
		for j in range(10):
			matrixInput = readFile('Input', str(i)+'-'+str(j)+'.txt')
			print '\n'
			for k in range(len(weightMatrix)):
				verifyNeuronio(weightMatrix,matrixInput,k,i,j)

	matrixInput = readFile('Input', 'A.txt')
	print '\n'
	for i in range(len(weightMatrix)):
		verifyNeuronio(weightMatrix,matrixInput,i,'A','A')

	matrixInput = readFile('Input', 'E.txt')
	print '\n'
	for i in range(len(weightMatrix)):
		verifyNeuronio(weightMatrix,matrixInput,i,'E','E')

	matrixInput = readFile('Input', 'T.txt')
	print '\n'
	for i in range(len(weightMatrix)):
		verifyNeuronio(weightMatrix,matrixInput,i,'T','T')		

	matrixInput = readFile('Input', 'H.txt')
	print '\n'
	for i in range(len(weightMatrix)):
		verifyNeuronio(weightMatrix,matrixInput,i,'H','H')

	matrixInput = readFile('Input', 'C.txt')
	print '\n'
	for i in range(len(weightMatrix)):
		verifyNeuronio(weightMatrix,matrixInput,i,'C','C')

	matrixInput = readFile('Input', 'N.txt')
	print '\n'
	for i in range(len(weightMatrix)):
		verifyNeuronio(weightMatrix,matrixInput,i,'N','N')

else: 
	print "This exercise doesn't exist"				