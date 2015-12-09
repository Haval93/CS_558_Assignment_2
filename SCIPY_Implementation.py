'''
CS 558

Authors: Haval Ahmed(815013661) and Ryan Stevens()

Assignment #2 Simulation #1

How To Run: Click Run and at the end of the simulation, there will be some console information as well
            as graphs to show statistical information.

First Order Equations:
dm/dt = 2m - ams, m(0) = m0
ds/dt = -s + ams, s(0) = s0

Variables For First Order Equation:
T = Time
M = M(t) is the number of mackerel
S = S(t) is the number of shark
A is a positive constant.

'''


from numpy import *
from scipy import integrate
from matplotlib import pyplot


# Initial Declarations
Mackerels = input("Insert A Number Of Mackerel In The System: ")
Sharks = input("Insert A Number Of Shark In The System: ")
A = input("Insert A Number For Constant: ")
Simulation_Time = input("Insert A Simulation Time: ")


# Initialization Array Of Values. M(T) and S(T) at T = 0
Initialization = [Mackerels, Sharks]

# We Want To Have A Function That Will Give Us The Rate Of Growth Over Time
def DX_DT(X, T = 0):

    return array([(2 * X[0]) - (A * X[0] * X[1]), (-X[1]) + (A * X[0] * X[1])])

# We Want A Time Variable For 0 To 60 Simulation Time
Time = linspace(0, Simulation_Time, Simulation_Time)

# Scipy's ODE Solver That Gives Us Growth Rate Over Time
X = integrate.odeint(DX_DT, Initialization, Time)

# Create A List For DM For Fish
fishList = X[:, 0]

# Create A List For DS For Sharks
sharkList = X[:, 1]

# Create A Total Amount of Fish During Simulation
fishPopulationTotal = sum(fishList)

# Create An Average Population Size For Fish Over Simulation Time
averageFishPopulationSize = fishPopulationTotal / Simulation_Time

# Get Max Population During Simulation
maxFishPopulationSize = max(fishList)

# Get Min Population During Simulation
minFishPopulationSize = min(fishList)

# Create A Total Amount of Sharks During Simulation
sharkPopulationTotal = sum(sharkList)

# Create An Average Population Size For Shark Over Simulation Time
averageSharkPopulationSize = sharkPopulationTotal / Simulation_Time

# Get Max Population During Simulation
maxSharkPopulationSize = max(sharkList)

# Get Min Population During Simulation
minSharkPopulationSize = min(sharkList)

# We want an eaten list
eatenList = list()

for i in range(0, Simulation_Time-1):
    fishEaten = fishList[i+1] - fishList[i]
    eatenList.append(fishEaten)

# Add Zero To First Thing In List
eatenList.insert(0, 0)

# Min/Max/Average Fish Eaten vs Born
minFishEaten = min(eatenList)
maxFishEaten = max(eatenList)
averageFishEaten = average(eatenList)

# Output Data

# Initialize System Values
print('Amount Of Mackerel Initially: ' + str(Mackerels))
print('Amount of Sharks Initially: ' + str(Sharks))

# Print Total Fish Population
print ('Total Amount Of Fish In System: ' + str(fishPopulationTotal))
# Print Total Shark Population
print('Total Amount Of Shark In System: ' + str(sharkPopulationTotal))
# Print Min Population For Fish During Simulation
print('Min Total Of Fish In System: ' + str(minFishPopulationSize))
# Print Max Population For Fish During Simulation
print('Max Total Of Fish In System: ' + str(maxFishPopulationSize))
# Print Min Population During Simulation
print('Min Total Of Shark In System: ' + str(minSharkPopulationSize))
# Get Max Population During Simulation
print('Max Total Of Shark In System: ' + str(maxSharkPopulationSize))
# Min/Max/Shark
print('Min Fish Eaten: ' + str(minFishEaten))
print('Max Fish Eaten: ' + str(maxFishEaten))
print('Average Fish Eaten: ' + str(averageFishEaten))


# We Want To Graph DM vs DS
pyplot.plot(X)
pyplot.xlabel("DM")
pyplot.ylabel("DS")
pyplot.show()

