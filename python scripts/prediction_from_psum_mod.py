#import subprocess

#import sys

import pandas as pd
import numpy as np

#argv = './' + sys.argv[1]
#filename = argv +".txt"

"""
f_append = open('/home/am/Videos/perceptronmod/perf_stat_record.txt', 'a+')

#df = pd.read_csv('perf_stat_record.txt', delimiter = '\t')

#f_append.close()
print("Reading text file into csv file")
df = pd.read_csv('/home/am/Videos/perceptronmod/perf_stat_record.txt', delimiter ='\t')
print("Saving the csv file")

df.to_csv('/home/am/Videos/perceptronmod/perf_stat_record.csv', index = None)
"""
print('Reading csv file')

df = pd.read_csv('/home/am/Desktop/Compark Project and Report/safeside-main/build/benchmarks/spectre_v1/perf_stat_record.csv', delimiter = '\t')


print (df.shape)
#print (df.head())
#print(df.iloc[1,0:301])


#print("Intitializing parameters")

m, n = df.shape # Excluding headers
print("Number of Total rows excluding headers = " + str(m) + "\n Number of columns including labels = "+ str(n))

#print(df.iloc[:,302])
#num_row_data = m-1 # Excluding header info

X = df.iloc[0:m,range(n-1)] 
xmax = np.max(X, axis =0)
#print( xmax)
#print("X = ", X)

X = np.where((np.max(X, axis=0)==0), X, (X*1./xmax))
#X = np.where(X[:,) == X, 
#print (X)
yframe = df.iloc[0:m, n-1]


x = np.array(X)
y = np.array(yframe)
y = y.reshape(m, 1)
print("y_true value")
print(y)
print("y shape= ", y.shape)
print("x shape: ", x.shape)

#print("Parameter Initialization")
#w = np.zeros((1, n-1))
#w = np.random.uniform(low=-1, high=1, size=(n-1))
#w = np.random.randn(1, n-1)*0.00001
#print(w)
learning_rate = 0.001
N = 100
K = 5;
w = np.zeros((K, n-1))

print("Training Phase")


z = np.zeros((m, K))
#print("p oringinal = \n", y)


for i in range(m):
    if y[i] == 1:
       z[i, 0] = 1
       z[i, 1:K] = -1
    elif y[i] == 2:
       z[i, 0] = -1
       z[i, 1] = 1           
       z[i, 2] = -1
       z[i, 3] = -1
       z[i, 4] = -1
    elif y[i] == 3:
       z[i, 0] = -1
       z[i, 1] = -1
       z[i, 2] =  1            
       z[i, 3] = -1
       z[i, 4] = -1
    elif y[i] == 4:
       z[i, 0:K-2] = -1
       z[i, K-2] = 1
       z[i, K-1] = -1
    elif y[i] == 5:
       z[i, 0:K-1] = -1
       z[i, K-1] =1
#print("Modified for multi-class = \n", z)

for iter in range(N):    
    #y_pred = np.dot(X, w)
    #p = np.concatenate((y, ), axis = 1)
    y_pred = np.dot(x, w.T)
    #print("y_pred=  ", y_pred)
    error = z-y_pred 
    #print("error = ", error)      
    #dw = (1/m)*np.dot(X.T, (y-y_pred).T)
    #w = w + learning_rate * dw       
    dw = np.dot(error.T, x)     
        
    #print("dw = ", dw)
    #print("Shape of dw = ", dw.shape)
    w = w +learning_rate*dw
    #print("w = ", w)
    #b[k] = dw
    #c[k] = w
                        
#print("dw = \n", dw)
#print("w=  \n", w) 
#print(b)
#print(y_pred)

print("Predicting") 
inp = input("Enter te rown number for the dataset example")
sample = x[int(inp), :]

p = np.dot(sample, w.T)
print ("prediction at x[in, :]= ", p)
p = np.max(p)
print ("prediction at x[in, :]= ", p)
pp = np.dot(sample, w.T)

y = 1+ np.argmax(pp, axis = 0)
pred = z[int(inp),y-1]

Attack_Type = {}
if y ==1: 
   Attack_Type [1] = "spectre_v1_pht_sa"
elif y == 2:
   Attack_Type[2] = "spectre_v1_btb_sa"
elif y == 3:
   Attack_Type[3] = "spectre_v1_btb_ca"
elif y == 4:
   Attack_Type[4] = "spectre_v4"
elif y == 5:
   Attack_Type[5] = "Unmitigated Workload/Benchmark"
   

   
print("Attack type = ", Attack_Type)

# Print train/test Errors
print(z[int(inp)])


print("train accuracy: {} %".format(100 -np.mean(np.abs(pred - z[int(inp)][y-1])) * 100))
           
        





    
    
