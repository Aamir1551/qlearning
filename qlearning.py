import random 

state0 = [[1,5], [2,2]] #stores tuples of type (newStateAfterTakingAction, rewardForaction)
state1 = [[0,3],[4,10]] 
state2 = [[3,20]] 
state3 = [[1,6]]
state4 = [[3,15]]


game = [state0, state1, state2, state3, state4] #game is composed of states

qstate0 = [[1,5], [2,2]] #stores tuples of type (newStateAfterTakingAction, predictedRewardForAction)
qstate1 = [[0,3],[4,10]] 
qstate2 = [[3,20]] 
qstate3 = [[1,6]]
qstate4 = [[3,15]]

qtable = [qstate0, qstate1, qstate2, qstate3, qstate4]

expRate = 1
learningRate = 0.8
discountRate = 0.8

def chooseAct(state):
	#returns action to take (pick action from set of action the state offers)
	#also returns the new state after picking the action 
	if(random.random() > expRate):
		#we are expoliting	
		maxVal = float("-inf") #stores the maximum reward recieved from taking action 
		actionNum = 0 #stores the action number of the action that gives the maximum reward
		newState = -1 #stores the new state after taking action actionNum 
		counter = 0 #keeps a track of what state we are checking 
		for tempActions in qtable[state]:
			if(maxVal < tempActions[1]):
				maxVal = tempActions[1]
				newState = tempActions[0]
				actionNum = counter 
			counter+=1
		return [actionNum, newState]
	else:
		randomAct = random.randint(0, len(game[state])-1) #picks a random action to take
		newState = qtable[state][randomAct][0] #stores the new state after taking the random action
		return[randomAct, newState]

def getReward(state, action):
	#return reward for picking action at a particular state
	return game[state][action][1]

def maxRewardFromState(state):
	maxReward = float("-inf")
	for tempActions in game[state]:
		if(tempActions[1] > maxReward):
			maxReward = tempActions[1]
	return maxReward 

def updateTable(state, action, reward, nxtState):
	currentQValue = qtable[state][action][1]
	currentQValue += learningRate * (reward + discountRate * (maxRewardFromState(nxtState)) - currentQValue)
	qtable[state][action][1] = currentQValue

def iterate(verbose = False):
	currentState = 0
	for j in range(0,4):
		[actionNum, newState] = chooseAct(currentState)
		reward = getReward(currentState, actionNum) 
		updateTable(currentState, actionNum, reward, newState)	
		currentState = newState	
		if(verbose == True):
			print(currentState)
currentState = 0
for i in range(1,100):
	iterate()
print(qtable)

expRate = 0
iterate(verbose=True)	
