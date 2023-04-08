#--------------PA 6: Concurrency--------------#
#--------------Name: Indronil Bhattacharjee--------------#
import random
import time
import threading

#--------------Task 1: Matrix Creation--------------#
N=int(input("Enter size of the Matrix: "))
print("For N =",N)

matrix=[]
for i in range(N):
    row=[]
    for j in range(N):
        row.append(random.randint(0,2**20))
    matrix.append(row)

#--------------Task 2: Without Threading--------------#
start1=time.time()
max1=float('-inf')
min1=float('inf')
sum1=0
count1=0

#Calculating max, min and avg value of the matrix
for i in range(N):
    for j in range(N):
        val=matrix[i][j]
        max1=max(max1,val)
        min1=min(min1,val)
        sum1 += val
        count1 += 1
avg1=sum1/count1
finish1=time.time()

print('Task 2:')
print('Max Value:', max1)
print('Min Value:', min1)
print('Average Value: {:.6f}'.format(avg1))
print('Time taken to compute max, min, and average: {:.6f} milliseconds'.format((finish1-start1)*10**3))

#--------------Task 3: With Threading--------------#
start2=time.time()
results=[None] * N
threads=[]

# Defining a function to calculate max, min and avg value of each row
def calculate (row, index, results):
    max2=max(row)
    min2=min(row)
    avg2=sum(row)/len(row)
    results[index]=(max2, min2, avg2)
    
# Creating and starting the threads
index=0
for row in matrix:
    thread=threading.Thread(target=calculate, args=(row,index,results))
    threads.append(thread)
    thread.start()
    index+=1

# Waiting for all the threads to be completed
for thread in threads:
    thread.join()

total_max=float('-inf')
total_min=float('inf')
total_sum=0

# Finding total max, min and avg 
for result in results:
    if result[0]>total_max:
        total_max=result[0]
    if result[1]<total_min:
        total_min=result[1]
    total_sum+=result[2]

total_avg=total_sum/len(results)
finish2=time.time()

print('Task 3:')
print('Max Value:', total_max)
print('Min Value:', total_min)
print('Average Value: {:.6f}'.format(total_avg))
print('Time taken to compute max, min, and average: {:.6f} milliseconds'.format((finish2-start2)*10**3))