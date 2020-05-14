import matplotlib.pyplot as plt
import math
import random
import time
import numpy as np


                        ###PLOTTING###
def plot(position,order,pop):
    plt.figure(figsize=(5,5))
    x,y=[],[]
    for i in range(0,len(position)):
        x.append(position[order[i]][0])
        y.append(position[order[i]][1])
        plt.text(position[order[i]][0],position[order[i]][1],position[order[i]][2],fontsize=8)
    plt.plot(x,y,'ro-' )
    plt.plot(x,y,'bo' ) 
    plt.axis('equal')
    plt.title(pop)
    plt.show()
      
def calcDistance(position,order):
    distance=0
    for i in range(len(order)-1):
        distance+= math.sqrt((position[order[i]][0]-position[order[i+1]][0])**2)+((position[order[i]][1]-position[order[i+1]][1])**2)
    return distance

def calcFitness(position,population):
    fitness=[]
    bestDistance=np.inf
    for i in range(len(population)):
        x=calcDistance(position,population[i])
        fitness.append(1/x);
        if x<bestDistance:
            bestOrder=population[i]
            bestDistance=x
    return bestOrder,fitness,bestDistance
def normalize(fitness):
    x=sum(fitness)
    for i in range(len(fitness)):
        fitness[i]/=x
    return fitness

def pickOne(population,fitness):
    x=random.random()
    index=0
    while(x>0):
        x=x-fitness[index]
        index+=1
    index-=1 
    return population[index]
def mutate(order,rate,n):
    for i in range(n):
        if(random.random()<rate):
            i=random.randint(0,len(order)-1)
            c= -1 if i==len(order)-1 else 1
            order[i],order[i+c]=order[i+c],order[i]
    return order
def cross(order1,order2):
    s=random.randint(0,len(order1)+1)
    e=random.randint(s,len(order1)+1)
    order1=order1[s:e]
    for i in order2:
        if i not in order1:
                  order1.append(i)
    return order1
def nextGen(population,fitness):
    newPopulation=[]
    for i in range(len(population)):
        order1=pickOne(population,fitness)
        order2=pickOne(population,fitness)
        order=cross(order1,order2)
        order=mutate(order,0.025,len(population))
        newPopulation.append(order)
    return newPopulation
height=30
width=30
c = int(input("\nEnter Number of cities(More Cities Increases Complexity): "))
count=0
position=[]
order=[]
while count<c:
    x = random.randint(0,width-2)
    y = random. randint(0,height-2)
    position.append((x,y,count))
    order.append(count)
    count+=1


                        ###Genetic Algorithm###
population=[]
temp=[]
fitness=[]
populationSize=1000
epoch=50
for i in range(populationSize):
    x=random.sample(order,len(order))
    population.append(x)
bd=[]
bestEver=np.inf
for i in range(epoch):
    bestOrder,fitness,bestDistance=calcFitness(position,population)
    fitness=normalize(fitness)
    population=nextGen(population,fitness)
    print(bestDistance)
    if bestDistance<bestEver:
        bestEver=bestDistance
        bestEverOrder=bestOrder
        ind=i+1
plot(position,bestEverOrder,ind)


