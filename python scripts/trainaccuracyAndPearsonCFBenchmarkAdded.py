#import subprocess

#import sys

import pandas as pd
import numpy as np


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

X_orig = df.iloc[0:m,range(n-1)] 
x_unnormalized = np.array(X_orig)
xmax = np.max(X_orig, axis =0)
#print( xmax)

X = np.where((np.max(X_orig, axis=0)==0), X_orig, (X_orig*1./xmax))
#X = np.where(X[:,) == X, 
#print (X)
yframe = df.iloc[0:m, n-1]


x = np.array(X)
y = np.array(yframe)
y = y.reshape(m, 1)

print("y shape= ", y.shape)
print("x shape: ", x.shape)

print("Parameter Initialization")
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
       z[i, 2] = 1            
       z[i, 3] = -1
       z[i, 4] = -1
    elif y[i] == 4:
       z[i, 0:K-2] = -1
       z[i, K-2] =1
       z[i, K-1] = -1
    elif y[i] == 5:
       z[i, 0:K-1] = -1
       z[i, K-1] = 1
print("Modified for multi-class = \n", z)

for itr in range(N):    
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
inp = input("Enter the row number for the dataset example")
sample = x[int(inp), :]

p = np.dot(sample, w.T)
print ("prediction at x[int, :]= ", p)
p = np.max(p)
print ("prediction at x[inp, :]= ", p)
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
   Attack_Type[5] = "unmitigated/Benchmark"
   
   

   
print("Attack type = ", Attack_Type)

# Print train/test Errors
print(z[int(inp)])
print("Calculating Training accuracy")


def index_true(i):
    #result = None
    for j in range(K):
        if z[i, j] == 1:
           result = j
    return result
    
def index_pred(i):
    example = x[i, :]
    b = np.dot(example, w.T)
    b_maxIndex = np.argmax(b, axis =0)
    
    return b_maxIndex   
    
    
def target_pred(i):
    example = x[i, :]
    b = np.dot(example, w.T)
    #b_maxIndex = np.argmax(b, axis =0)
    b_max = max(b)
    
    
    return b_max  
        
    

#real_train = []
#pred_train = []
real_train = np.zeros((m, 1))
pred_train = np.zeros((m, 1))

for training_set in range(m):
    
    ind_true = index_true(training_set)
    real_train[training_set] = z[training_set, ind_true]
    ind_pred = index_pred(training_set)
    pred_train[training_set] = z[training_set, ind_pred] 
    
    
    
#print("pred_train=  \n", pred_train)
#print("real_train=  \n", real_train)

#print ("Error =", pred_train - real_train)


print("Train accuracy: {} %".format(100 -np.mean(np.abs(pred_train - real_train) * 100)))



print("Separating dataset into their respective attack variant")
spectre_v1_pht_sa = []
spectre_v1_btb_sa = []
spectre_v1_btb_ca = []
spectre_v4 = []

unmitigated = []

v1_pht_sa_target = []
v1_btb_sa_target = []
v1_btb_ca_target = []
v4_target  = []

unmitigated_target = []


for row in range(m):
    if z[row, 0] == 1:      
       spectre_v1_pht_sa.append(x[row, :])
       v1_pht_sa_target.append(target_pred(row))
    elif z[row, 1] == 1:
       spectre_v1_btb_sa.append(x[row, :])
       v1_btb_sa_target.append(target_pred(row))
    elif z[row, 2] == 1:
       spectre_v1_btb_ca.append(x[row, :])
       v1_btb_ca_target.append(target_pred(row))
    elif z[row, 3] == 1:      
       spectre_v4.append(x[row, :])
       v4_target.append(target_pred(row))
    elif z[row, 4] == 1:      
       unmitigated.append(x[row, :])
       unmitigated_target.append(target_pred(row))

print("Finding the pearson Correlation Coefficient for each attack type")

import statistics

spectre_v1_pht_sa_array = np.array(spectre_v1_pht_sa)
v1_pht_sa_target_array = np.array(v1_pht_sa_target)
#print("v1_pht_sa_target_array =\n", v1_pht_sa_target_array )

spectre_v1_btb_sa_array = np.array(spectre_v1_btb_sa)
v1_btb_sa_target_array = np.array(v1_btb_sa_target)

spectre_v1_btb_ca_array = np.array(spectre_v1_btb_ca)
v1_btb_ca_target_array = np.array(v1_btb_ca_target)

spectre_v4_array = np.array(spectre_v4)
v4_target_array = np.array(v4_target)

unmitigated_array = np.array(unmitigated)
unmitigated_target_array = np.array(unmitigated_target)

spectre_v1_pht_sa_array_mean = np.zeros(((n-1)))
spectre_v1_btb_sa_array_mean = np.zeros(((n-1)))
spectre_v1_btb_ca_array_mean = np.zeros(((n-1)))
spectre_v4_array_mean = np.zeros(((n-1)))
unmitigated_array_mean = np.zeros(((n-1)))

spectre_v1_pht_sa_array_sd = np.zeros((n-1))
#leng = len(v1_pht_sa_target_array)
#v1_pht_sa_target_array_sd = np.zeros((len(v1_pht_sa_target_array)))
v1_pht_sa_target_array_mean = statistics.mean(v1_pht_sa_target_array.flatten())
v1_pht_sa_target_array_sd = statistics.stdev(v1_pht_sa_target_array.flatten())

p1 = np.zeros((n-1))
p2 = np.zeros((n-1))
p3 = np.zeros((n-1))
p4 = np.zeros((n-1))
p5 = np.zeros((n-1))
from scipy.stats import pearsonr
for col in range(n-1):
    spectre_v1_pht_sa_array_mean[col] =  sum(spectre_v1_pht_sa_array[:, col])/len(spectre_v1_pht_sa_array)
    spectre_v1_btb_sa_array_mean[col] =  sum(spectre_v1_btb_sa_array[:, col])/len(spectre_v1_btb_sa_array)
    spectre_v1_btb_ca_array_mean[col] =  sum(spectre_v1_btb_ca_array[:, col])/len(spectre_v1_btb_ca_array)
    spectre_v4_array_mean[col] =  sum(spectre_v4_array[:, col])/len(spectre_v4_array)
    unmitigated_array_mean[col] =  sum(unmitigated_array[:, col])/len(unmitigated_array)
    
    spectre_v1_pht_sa_array_sd = statistics.stdev(spectre_v1_pht_sa_array[:,col])
    spectre_v1_btb_sa_array_sd = statistics.stdev(spectre_v1_btb_sa_array[:,col])
    spectre_v1_btb_ca_array_sd = statistics.stdev(spectre_v1_btb_ca_array[:,col])
    spectre_v4_array_sd = statistics.stdev(spectre_v4_array[:,col])
    unmitigated_array_sd = statistics.stdev(unmitigated_array[:,col])
   
    p1[col], _ = pearsonr(spectre_v1_pht_sa_array[:, col], v1_pht_sa_target_array)
    p2[col], _ = pearsonr(spectre_v1_btb_sa_array[:, col], v1_btb_sa_target_array)
    p3[col], _ = pearsonr(spectre_v1_btb_ca_array[:, col], v1_btb_ca_target_array)
    p4[col], _ = pearsonr(spectre_v4_array[:, col], v4_target_array)
    p5[col], _ = pearsonr(unmitigated_array[:, col], unmitigated_target_array)
    


print("v4_target_array = \n", v4_target_array)
#print("spectre_v1_pht_sa_array avearge = \n", spectre_v1_pht_sa_array_mean)
print(" spectre_v4_array_sd = \n",  spectre_v4_array_sd)

print("Shape of spectre_v4_array_mean = \n", spectre_v4_array_mean.shape)

#print("Pearson Correlation Coefficient of spectre_v1_pht_sa = \n", p1)
print("Length of p4 = \n", len(p4))

idx = np. argpartition(p4, -30)[30:]
#indices = idx[np. argsort((-p1)[idx])]
indices = np.argsort(p4)
#file1 = open("/home/am/Videos/perceptronmod/sp_v1_imp_feature", 'w')
#for i in range(n-1):
 #   if p1[i] > 0.8 and p1[i] < 0.99:
  #     file1.write(str(i) + "\t")

print("Coff in Descending order = \n", p4[indices])
#print("idx = \n", idx)
print("indices = \n", indices)
print("Highest Value= \n", p4[254])
print("X value at col =10 = \n", x[:,254])
