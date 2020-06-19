import matplotlib.pyplot as plt
import turtle
import math
import numpy as np
import pylab
import random
from scipy.integrate import quad

# Task 1
def get_distance_1D(choice , numSteps , prob , x, y):
  steps = np.random.choice(choice , numSteps , p = prob)
  exp = 0
  for i in range(len(choice)):
    exp  += choice[i]*prob[i]
  expected_dist = exp*numSteps

  lst = []
  x = x
  for cord in steps:
    x += cord
    lst.append(x) 
  y_ = []
  for  i in range(numSteps):
    y_.append(i)
  dist = np.sum(steps)
  # return (dist*dist)**0.5
  return ((expected_dist**2)**0.5 , (dist*dist)**0.5 , y_ , lst)

# call task 1 and plot

# a = get_distance_1D([-1,0,1], 50 , [0.2,0.2,0.6] ,0 , 0)
# b = get_distance_1D([-1,0,1],  50, [0.2,0.2,0.6] ,0 , 0)
# c = get_distance_1D([-1,0,1], 50 , [0.2,0.2,0.6] ,0 , 0)
# d = get_distance_1D([-1,0,1], 50 , [0.2,0.2,0.6] ,0 , 0)
# e = get_distance_1D([-1,0,1], 50 , [0.2,0.2,0.6] ,0 , 0)
# f = get_distance_1D([-1,0,1], 50 , [0.2,0.2,0.6] ,0 , 0)
# pylab.plot(a[2],a[3],'-b' )
# pylab.plot(b[2],b[3], '-r'  )
# pylab.plot(c[2],c[3] ,'-y' )
# pylab.plot(d[2],d[3] ,'-g' )
# pylab.plot(f[2],f[3] , '-p')
# pylab.plot(e[2],e[3]  ,'-c')
# print('Expected Distance according to model: ' + str(a[0]))
# print('Average of the  Distance covered: '+ str((a[1]+b[1]+c[1]+d[1]+e[1]+f[1])/6))

# pylab.legend()

# Task 4
def get_distance_1D_cont(numSteps, x, y):
  steps = [x] 
  for  i in range(numSteps):
    x += random.uniform(0,1)
    steps.append(x)

  
  y_ = [i for i in range(numSteps+1)]
  dist = steps[-1]
  return ((dist*dist)**0.5 , 0.5*numSteps , y_ , steps)

# call task 4 and plot

# a = get_distance_1D_cont(30 , 0,0)
# b = get_distance_1D_cont(30 , 0,0)
# c = get_distance_1D_cont(30 , 0,0)
# d = get_distance_1D_cont(30 , 0,0)
# e = get_distance_1D_cont(30 , 0,0)
# f = get_distance_1D_cont(30 , 0,0)
# pylab.plot(a[2],a[3],'-b' )
# pylab.plot(b[2],b[3], '-r'  )
# pylab.plot(c[2],c[3] ,'-y' )
# pylab.plot(d[2],d[3] ,'-g' )
# pylab.plot(f[2],f[3] , '-p')
# pylab.plot(e[2],e[3]  ,'-c')
# print('Expected Distance according to model: ' + str(a[1]))
# print('Average of the  Distance covered: '+ str((a[0]+b[0]+c[0]+d[0]+e[0]+f[0])/6))

# Task 2 

def get_meeting_point(walk1_x, walk2_x):
  x_1 = walk1_x
  x_2 = walk2_x
  y_1 = 0 
  y_2 = 0 
  # x_1+= random.choice([-1, 1])
  # x_2+= random.choice([-1, 1])
  x_1_list = [x_1]
  x_2_list = [x_2]
  num_steps = [1]
  x = 1
  while(x_1!=x_2):
    x+=1
    num_steps.append(x)
    x_1+= random.choice([-1, 1])
    x_1_list.append(x_1)
    x_2+= random.choice([-1, 1])
    x_2_list.append(x_2)
  y =[]
  for i in range(len(x_1_list)):
    y.append(0)

  pylab.plot(num_steps ,x_1_list , 'b--')
  pylab.plot(num_steps ,x_2_list )
  print('no of steps:' + str(x))
  return x

# Call task 2 and plot

# res={}
# for i in range(100):
#     res[i]=0
# for i in range(100):
#     a = get_meeting_point(0,6)
#     if a in res.keys():
#         res[a]=res[a]+1
        
# res.pop(0)

# fig, ax = plt.subplots()

# ax.bar(list(res.keys()), list(res.values()))
# plt.suptitle('frequency of how much time it took for\ntwo people to cross paths', fontsize=16)

# plt.ylabel('frequency')
# plt.xlabel('time/steps')
# plt.show()

# Task 8
def task_08():
  no_of_steps = 0
  node_1,node_2= [(random.randint(-100,100),random.randint(-100,100))], [(random.randint(-100,100),random.randint(-100,100))]
  e_dist = math.sqrt((node_1[-1][0]-node_2[-1][0])**2 + (node_1[-1][1]-node_2[-1][1])**2)
  while not (0 < e_dist < 1):
    x, y = node_1[-1]
    x_2, y_2 = node_2[-1]

    # old_x , old_y = x, y 
    # old_x2 , old_y2 = x_2, y_2 
    step, step2 = random.uniform(0,1), random.uniform(0,1)
    angle, angle2 = random.uniform(0,360),random.uniform(0,360)
    # new coordinates
    new_x1 , new_y1 = x+(step* math.cos(angle)) , y+ (step* math.sin(angle))
    new_x2 , new_y2 = x_2+(step2* math.cos(angle2)) , y_2+ (step2* math.sin(angle2))
      
    if math.sqrt((new_x1)**2 + (new_y1)**2) < 100:
      node_1.append((new_x1,new_y1))
    else:
      node_1.append((-x,-y))
    if math.sqrt((new_x2)**2 + (new_y2)**2) < 100:
      node_2.append((new_x2, new_y2))
    else:
      node_2.append((-x_2,-y_2))
    if no_of_steps < 10000:
      no_of_steps+=1
    else:
      return -1
    e_dist = math.sqrt((node_1[-1][0]-node_2[-1][0])**2 + (node_1[-1][1]-node_2[-1][1])**2)
  return no_of_steps
                   
def simulations(no_sim):
  histogram = []
  for i in range(no_sim):
    steps = task_08()
    if steps!= -1:
      histogram.append(steps)
  return histogram

# call task 8 and plot

no_of_simulations = 1000
data = simulations(no_of_simulations)
print(data)
n,bins, patches = plt.hist(data, color='r', edgecolor='k', alpha=0.65)

print("Expected Value: ", round(sum(data)/len(data), 2))

plt.xlabel("number of steps")
plt.ylabel("frequency")
plt.show()             
