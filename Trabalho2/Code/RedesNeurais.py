def readFile(fileName):
	file = open('../Input/'+fileName, 'r')
	body = file.read()
	file.close()
	inputZero = range(30) 
	
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

#def train():

matrix = createMatrix(6,30)
matrix = fillMatrix()

print(matrix)	

