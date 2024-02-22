# Chirag Nambiar
# Project on 1 Dimensional Random Walk

import numpy as np
import matplotlib.pyplot as plt


n=1000                              		# Number of iterations and steps

x_pos=np.arange(-n,n)               	# The range of all possible positions in x axis
count=np.zeros(2*n)                	# An array to store the frequency of different positions and their probability
x_final=np.zeros(n)                       	# An array to store the final position after each iteration

for i in range(n):                  		# Iterations loop
    x=np.zeros(n+1)                 	# An array to store position after each step
    start=0
    x[0]=start                      			# Defining initial position 
    for j in range (1,n+1):         			# Steps loop
        p=np.random.randint(2,4)    		# 2=Tails, moves left. 3=Heads, moves right
        if p%2!=0:
            x[j]=start+1
        else:
            x[j]=start-1
        start=x[j]
    x_final[i]=x[j]
    if i==0:                        			# Plotting Positions vs Steps for one iteration
        plt.plot(np.arange(n+1), x)
        plt.title("Position vs Steps\n(Single Iteration)")
        plt.xlabel("Steps")
        plt.ylabel("Position")
        plt.show()   
        #plt.savefig("Position vs Steps_CP_Project")
	

for i in range(-n,n):               # Calculating frequency of positions
    for j in x_final:
        if i==j:
            count[i+n]+=1

count/=2*n                                                      	# Computing approximate probability
actual_prob = (1/np.sqrt(2*np.pi*n))*np.exp(-(x_pos**2/(2*n))) # Computing actual probability

plt.plot(x_pos, count, '.', label="Approximate Probability Distribution")
plt.plot(x_pos, actual_prob, label="Actual Probability Distribution")
plt.title("Probability distribution\n(All Iterations)")
plt.legend()
plt.xlabel("Position")
plt.ylabel("Probability")
plt.show()
#plt.savefig("Probability Distribution_CP_Project")
