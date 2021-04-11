import numpy as np
import matplotlib.pyplot as plt 
from array import *

np_possibles = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
final = np.empty((10,10), int)

#Max_value_loop is the largest possible ans for the three values generated(can alter)
max_value_loop = [10,10,10]

#Controlling the number of solutions generated(can alter)
tries = 5

#Prep: Putting cases into boxes
def calculate(result):
    key = 0 
    i = 0
    k = 0
    j = 0
    gotcha = 0
    
    final.fill(0)
    for i in range(count):
        while j < case_count[i]:
            temp = result[k]
            final[i,j] = temp
            k = k + 1
            j = j + 1
        i = i + 1
        j = 0
    #print(final)

    for i in range(0, count-1):
        if(final[i, case_count[i]-1] == final[i+1, 0]):
            return 0
    return 1

def print_ans(i, k, j, result):
    print(final)
    for end in range(0, count):
      print("The range for case " + str(end+1) + " is between: " + str(final[end, 0]) + " to " + str(final[end, case_count[end]-1]) )

    print("The value for each case is: " + str(i) + ", " + str(k) + ", " + str(j))
    np_result = np.array(result)
    plt.hist(np_result, bins = count)
    plt.show()
    


#First step: User inputs
case_name = []
case_count = []
count = int(input("How many case do you want? "))
for i in range(count):
    name = input("What is the name for case " + str(i+1) + "? ")
    case_name.append(name)
    data = int(input("How many possibilities do you want in case " + str(i+1) + "? "))
    case_count.append(data)
    print("Case name " + "'" + case_name[i] + "'" + " recorded...")
    print("Case possibilities " + "'" + str(case_count[i]) + "'" + " recorded...\n")

#Second step: Looping

key = 0
chance = 0
while key != 1:
    np_sample = np_possibles.copy()

    for i in range(1, max_value_loop[0]):      
        if(key == 1 and chance == tries):
            break

        for k in range(1, max_value_loop[1]):
            if(key == 1 and chance == tries):
                break

            for j in range(1, max_value_loop[2]):
                np_sample[:,1] = np_sample[:,1] * k
                np_sample[:,0] = np_sample[:,0] * i
                np_sample[:,2] = np_sample[:,2] * j
                result = []
                for n in range(0, 8):
                    temp = np_sample[n,0] + np_sample[n,1] + np_sample[n,2]
                    result.append(temp)
                result.sort()
            
                gotcha = calculate(result)
                if(gotcha == 1):
                    key = 1
                    chance = chance + 1
                    print_ans(i, k, j, result)
                    if(chance == tries):
                        break
                
                np_sample = np_possibles.copy()

 


