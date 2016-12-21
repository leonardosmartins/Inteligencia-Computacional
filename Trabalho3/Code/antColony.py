
import time
import sys
from random import randint
from math import exp, sqrt

def readDistanceMatrix(fileName):
  file = open('../input/'+fileName, 'r')
  matrix = []
  matrix = [ line.split() for line in file ]
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      matrix[i][j] = float(matrix[i][j])
  
  anotherMatrix = createMatrix(len(matrix), len(matrix[0]), 0)      
  
  #filling upper diagonal
  for i in range(len(anotherMatrix)):
    for j in range(i, len(anotherMatrix[0])):
      anotherMatrix[i][j] = matrix[i][j-i]
      
  #filling simetrical diagonal
  for i in range(len(anotherMatrix)):
    for j in range(i):
      anotherMatrix[i][j] = anotherMatrix[j][i]       
  return anotherMatrix

def readEuclideanMatrix(fileName):
  file = open('../input/'+fileName, 'r')
  euclideanPointsMatrix= []
  euclideanPointsMatrix= [ line.split() for line in file ]
  for i in range(len(euclideanPointsMatrix)):
    for j in range(len(euclideanPointsMatrix[i])):
      euclideanPointsMatrix[i][j] = float(euclideanPointsMatrix[i][j])
  
  matrix = createMatrix(len(euclideanPointsMatrix), len(euclideanPointsMatrix), 0)

  for i in range(len(euclideanPointsMatrix)):
    for j in range(len(euclideanPointsMatrix)):
      matrix[i][j] = sqrt(pow(euclideanPointsMatrix[i][0]-euclideanPointsMatrix[j][0],2) + pow(euclideanPointsMatrix[i][1]-euclideanPointsMatrix[j][1],2))
  return matrix

def createMatrix(lin, col, initialValue):
  matrix = []
  for i in range(lin):
    matrix.append( [initialValue] * col )
  return matrix

def startAnt(matrix):
  for i in range(len(matrix)):
    matrix[i][i] = 1
  return matrix
    
def calculeProbability(probMatrix, pathMatrix, pheromMatrix, distMatrix, A, B):
  for i in range(len(probMatrix)):
    for j in range(len(probMatrix[0])):
      if(pathMatrix[i][j] == 0):
        probMatrix[i][j] = probij(pheromMatrix, distMatrix, i, j, A, B)        
  return probMatrix 
  
def probij(pheromMatrix, distMatrix, i, j, A, B):
  sum = 0
  for k in range(len(pheromMatrix[0])):
    if(pathMatrix[i][k] == 0):
      sum += ((pheromMatrix[i][k] ** A) * (1.0/(distMatrix[i][k]) ** B))
  return ((pheromMatrix[i][j] ** A) * (1.0/(distMatrix[i][j])**B)) / sum

def draftNextCity(probMatrix, pathMatrix):
  lista = []
  vetCity = range(len(probMatrix))
  for i in range(len(probMatrix)):
    number = randint(1,999)/1000.0
    lista.append(number)
    vet = range(len(probMatrix[i]))
    vet[0] = probMatrix[i][0]
    
    for v in range(1,len(vet)):
      vet[v] = vet[v-1]+probMatrix[i][v]
    for v in range(len(vet)):
      if number <= vet[v]:
        vetCity[i] = v
        break
  return vetCity
  
def fillPathMatrix(vetCity, pathMatrix):
  for i in range(len(pathMatrix)):
   	aux = max(pathMatrix[i])
    	pathMatrix[i][vetCity[i]] = aux + 1
  return pathMatrix

def sub(distanceMatrix, pathMatrix, pheromoneMatrix, A, B):

  
  for i in range(len(distanceMatrix)-1):
    probabilityMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 0)
    probabilityMatrix = calculeProbability(probabilityMatrix, pathMatrix, pheromoneMatrix, distanceMatrix, A, B)
    vetCity = draftNextCity(probabilityMatrix, pathMatrix)
    pathMatrix = fillPathMatrix(vetCity, pathMatrix)
    
  return pathMatrix

def calculateFinalDistance(pathMatrix, distanceMatrix):
  vet = range(len(distanceMatrix))  
  for i in range(len(pathMatrix)):
    lista = []
    for k in range(1,len(pathMatrix)+1):
      for j in range(len(pathMatrix[i])):
        if pathMatrix[i][j] == k:
          lista.append(j)
          break
    lista.append(lista[0])
    vet[i] = distanceMatrix[i][lista[0]]
    for z in range(1,len(lista)):
      vet[i] += distanceMatrix[lista[z-1]][lista[z]]
  return vet

def calculatePheromone(pathMatrix, pheromoneMatrix, distanceVector, p):
  for i in range(len(pheromoneMatrix)):
    for j in range(len(pheromoneMatrix[0])):
      pheromoneMatrix[i][j] = (1-p) * pheromoneMatrix[i][j] + verifyPheromone(i,j, 10.0, pathMatrix, distanceVector)
  return pheromoneMatrix
      
      
def verifyPheromone(i,j,Q, pathMatrix, distanceVector):
  sum = 0
  for k in range(len(pathMatrix)):
    aux = abs(pathMatrix[k][i] - pathMatrix[k][j]) 
    if(aux == 1):
      sum += Q/distanceVector[k]
  return sum
         
def verifyPaths(pathMatrix):
  vet = range(len(pathMatrix))
  for i in range(len(pathMatrix)):
    lista = []
    for k in range(1,len(pathMatrix)+1):
      for j in range(len(pathMatrix[i])):
        if pathMatrix[i][j] == k:
          lista.append(j)
          break
    lista.append(lista[0])
    vet[i] =  lista
  
  
  for i in range(1,len(vet[0])):
    aux = 0
    for j in range(1,len(vet)):
      for k in range(1,len(vet[0])):
        
        if((vet[j][k-1] == vet [0][i-1] and vet[j][k] == vet[0][i]) or (vet[j][k-1] == vet [0][i] and vet[j][k] == vet[0][i-1])):
          aux += 1
          break      
    if (aux != len(vet)-1):
      return -1
  
  return 1         

if (sys.argv[1]) == "1":
	for i in range(0,int(sys.argv[2])):
		distanceMatrix = readDistanceMatrix("M6")
		pheromoneMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 1)

		for j in range(0,int(sys.argv[3])):
  			pathMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 0)
  			pathMatrix = startAnt(pathMatrix)  
  			pathMatrix = sub(distanceMatrix, pathMatrix, pheromoneMatrix, int(sys.argv[5]), int(sys.argv[6]))
  			distanceVector = calculateFinalDistance(pathMatrix, distanceMatrix)
  			pheromoneMatrix = calculatePheromone(pathMatrix, pheromoneMatrix, distanceVector, float(sys.argv[4]))
  			if verifyPaths(pathMatrix) == 1:
    				break
    				
		minDistance = min(distanceVector)
		for j in range(len(distanceVector)):
  			if(distanceVector[j] == minDistance):
   				print "\n-------------------- ITERACAO "+ str(i)+" --------------------"
    				print "Melhor caminho: "+str(pathMatrix[j])
    				print "Distancia total do melhor caminho: "+str(minDistance)
    				break      

elif (sys.argv[1]) == "2":
	for i in range(0,int(sys.argv[2])):
		distanceMatrix = readEuclideanMatrix("M15")
		pheromoneMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 1)

		for j in range(0,int(sys.argv[3])):
  			pathMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 0)
  			pathMatrix = startAnt(pathMatrix)  
  			pathMatrix = sub(distanceMatrix, pathMatrix, pheromoneMatrix, int(sys.argv[5]), int(sys.argv[6]))
  			distanceVector = calculateFinalDistance(pathMatrix, distanceMatrix)
  			pheromoneMatrix = calculatePheromone(pathMatrix, pheromoneMatrix, distanceVector, float(sys.argv[4]))
  			if(verifyPaths(pathMatrix) == 1):
    				break

		minDistance = min(distanceVector)
		for j in range(len(distanceVector)):
  			if(distanceVector[j] == minDistance):
  				print ("\n-------------------- ITERACAO "+ str(i)+" --------------------")
    				print ("Melhor caminho: "+str(pathMatrix[j]))
    				print "Distancia total do melhor caminho: "+str(minDistance)
    				break

elif (sys.argv[1]) == "3":
	for i in range(0,int(sys.argv[2])):
		distanceMatrix = readEuclideanMatrix("M29")
		pheromoneMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 1)

		for j in range(0,int(sys.argv[3])):
  				pathMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 0)
  				pathMatrix = startAnt(pathMatrix)  
  				pathMatrix = sub(distanceMatrix, pathMatrix, pheromoneMatrix, int(sys.argv[5]), int(sys.argv[6]))
  				distanceVector = calculateFinalDistance(pathMatrix, distanceMatrix)
  				pheromoneMatrix = calculatePheromone(pathMatrix, pheromoneMatrix, distanceVector, float(sys.argv[4]))
  				if(verifyPaths(pathMatrix) == 1):
    					break

		minDistance = min(distanceVector)
		for j in range(len(distanceVector)):
  			if(distanceVector[j] == minDistance):
  				print ("\n-------------------- ITERACAO "+ str(i)+" --------------------")
    				print ("Melhor caminho: "+str(pathMatrix[j]))
    				print "Distancia total do melhor caminho: "+str(minDistance)
    				break

elif (sys.argv[1]) == "4":
	for i in range(0,int(sys.argv[2])):
		distanceMatrix = readEuclideanMatrix("M38")
		pheromoneMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 1)

		for j in range(0,int(sys.argv[3])):
  			pathMatrix = createMatrix(len(distanceMatrix), len(distanceMatrix[0]), 0)
  			pathMatrix = startAnt(pathMatrix)  
  			pathMatrix = sub(distanceMatrix, pathMatrix, pheromoneMatrix, int(sys.argv[5]), int(sys.argv[6]))
  			distanceVector = calculateFinalDistance(pathMatrix, distanceMatrix)
  			pheromoneMatrix = calculatePheromone(pathMatrix, pheromoneMatrix, distanceVector, float(sys.argv[4]))
  			if(verifyPaths(pathMatrix) == 1):
    				break

		minDistance = min(distanceVector)
		for j in range(len(distanceVector)):
  			if(distanceVector[j] == minDistance):
  				print ("\n-------------------- ITERACAO "+ str(i)+" --------------------")
    				print ("Melhor caminho: "+str(pathMatrix[j]))
    				print "Distancia total do melhor caminho: "+str(minDistance)
    				break

else: 
	print "This exercise doesn't exist"    	    	    	