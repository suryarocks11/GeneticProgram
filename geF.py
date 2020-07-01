import random
import numpy as np
from numpy.random import choice
import pandas as pd
mutationRate = 0.01
totalPopulation = 150
crossOver = 0.5
target = "winner"
alpha_list = [chr(x) for x in range(ord('a'), ord('z') + 1)] 
alpha_list.append(' ')
populationData = []
fitnessData = []
secure_random = random.SystemRandom()
for outloop in range(totalPopulation):
  randomData = []
  fitnessScore = 0
  for inloop in range(len(target)):
    selectedData = secure_random.choice(alpha_list)
    if (selectedData == target[inloop]):
      fitnessScore = fitnessScore + 1
    randomData.append(selectedData)
  populationData.append(randomData)
  fitnessData.append(fitnessScore)
probabilityDist = []
for outloop in range(totalPopulation):
  probabilityDist.append(fitnessData[outloop]/len(target))
probDataFrame = pd.DataFrame({'String':populationData,'FitnessScore':fitnessData,'Probability':probabilityDist})
probDataFrame = probDataFrame.sort_values(['Probability'],ascending=False)
probDataFrame = probDataFrame.reset_index(drop=True)
def maxProb(probabilityDist):
  probabilityList = [f for f in set(probabilityDist)]
  return (probabilityList[len(probabilityList)-2])
def getFitnessScore(data):
    data = ''.join([elem for elem in data])
    fitnessScore = 0
    for inloop in range(len(target)):
      if (data[inloop] == target[inloop]):
        fitnessScore = fitnessScore + 1
    return fitnessScore


def viewElement(data):
    data = ''.join([elem for elem in data])
    return data



crossOverPoint = int(crossOver*len(target))
generationCount = 5000
for loop in range(generationCount):
  draw=[]
  draw.append(probDataFrame[0:1]["String"].values[0])
  draw.append(probDataFrame[1:2]["String"].values[0])
  #print('Fitness Scores of Parents ',getFitnessScore(draw[0]),getFitnessScore(draw[1]))
  if (getFitnessScore(draw[0])==len(target) | getFitnessScore(draw[1])==len(target)):
    print(viewElement(draw[0]),' ',viewElement(draw[1]))
    break
  child1 = draw[0][0:crossOverPoint]+draw[1][crossOverPoint:]
  child2 = draw[1][0:crossOverPoint]+draw[0][crossOverPoint:]
  child1[random.randint(0,len(target)-1)] = secure_random.choice(alpha_list)
  child2[random.randint(0,len(target)-1)] = secure_random.choice(alpha_list)
  populationData.append(child1)
  populationData.append(child2)
  fitnessData = []
  totalPopulation = len(populationData)
  for outloop in range(totalPopulation):
    fitnessScore = getFitnessScore(populationData[outloop])
    fitnessData.append(fitnessScore)
  probabilityDist = []
  for outloop in range(totalPopulation):
    probabilityDist.append(fitnessData[outloop]/sum(fitnessData))
  probDataFrame = pd.DataFrame({'String':populationData,'FitnessScore':fitnessData,'Probability':probabilityDist})
  probDataFrame = probDataFrame.sort_values(['Probability'],ascending=False)
  probDataFrame = probDataFrame.reset_index(drop=True)
  print('Generation ',loop,' ',' Average Fitness Score ',probDataFrame["FitnessScore"].mean(),' ', ''.join(elem for elem in child1),' ',getFitnessScore(child1),''.join(elem for elem in child2),getFitnessScore(child2))
  #print('Generation ',loop,' ',' Average Fitness Score ',probDataFrame["FitnessScore"].mean())    
