import time

def readFile(fileName):
	file = open('../Input/'+fileName, 'r')
	body = file.read()
	file.close()
	inputZero = range(31) 
	inputZero[30] = 0

	for i in range(30):
		inputZero[i] = int (body[i*2])

	return inputZero

def createMatrix(lin, col):
	matrix = []
	for i in range(lin):
		matrix.append([0] * col)

	return matrix

def fillMatrix():
	for i in range(6):
		matrix[i] = readFile(str(i)+'.txt')

	return matrix	

def train(neuronio,weightMatrix, matrix):
	verifyInput = range(6)
	verifyEnd = 1
	epoch = 0

	while(verifyEnd != 0):
		epoch += 1
		for j in range(6):
			result = 0
			for i in range(len(weightMatrix[0])):
				result = result + weightMatrix[neuronio][i] * matrix[j][i]

			if result > 0:
				result = 1
			else:
				result = 0		
	
			if result == 0 and j == neuronio:
				for i in range(len(weightMatrix[0])):
					weightMatrix[neuronio][i] = weightMatrix[neuronio][i] + matrix[j][i]

				verifyInput[j] = 1			

			elif result == 1 and j != neuronio:		
				for i in range(len(weightMatrix[0])):
					weightMatrix[neuronio][i] = weightMatrix[neuronio][i] - matrix[j][i]
				
				verifyInput[j] = 1			

			else:
				verifyInput[j] = 0

		verifyEnd = 0
		for i in range(len(verifyInput)):
			verifyEnd = verifyEnd + verifyInput[i] 					
	
	print "Neuronio",neuronio,"Epocas necessarias para treinar:",epoch
	return weightMatrix			

def verifyNeuronio(weightMatrix, matrix, neuronio):
	for j in range(6):
		result = 0
		for i in range(len(weightMatrix[0])):
			result = result + weightMatrix[neuronio][i] * matrix[j][i]

		if result > 0:
			result = 1
		else:
			result = 0

		print "Neuronio:",neuronio,"Entrada:",j,"Resultado",result			

matrix = createMatrix(6,31)
matrix = fillMatrix()

weightMatrix = createMatrix(6,31)

weightMatrix[0][30] = 1
weightMatrix[1][30] = 1
weightMatrix[2][30] = 1
weightMatrix[3][30] = 1
weightMatrix[4][30] = 1
weightMatrix[5][30] = 1

for i in range(len(weightMatrix)):
	weightMatrix = train(i,weightMatrix,matrix)

for i in range(len(weightMatrix)):
	verifyNeuronio(weightMatrix,matrix,i)
#print(weightMatrix)

# print(matrix)	

