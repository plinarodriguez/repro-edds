# Libraries
import pandas as pd
import numpy as np
# SIMULATION NOMINAL
# --------------- 
# Nominal Model for low inlet velocity 
nominal = pd.read_csv("data/simulation/nominal/S0_G0_V0_063.csv") 
center = nominal[' Y [ m ]'][0] + 0.008 # Scale to center at 0
# -------------------------------------------------------------------
# SIMULATION SAMPLING 
# --------------- 
# Simulation Samples
sim1 = pd.read_csv("data/simulation/samples/S1_G1_V0_063.csv") 
sim2 = pd.read_csv("data/simulation/samples/S2_G2_V0_063329.csv") 
sim3 = pd.read_csv("data/simulation/samples/S3_G3_V0_0642.csv") 
center1 = sim1[' Y [ m ]'][0] + 0.008 # Scale to center at 0
center2 = sim2[' Y [ m ]'][0] + 0.008 # Scale to center at 0
center3 = sim3[' Y [ m ]'][0] + 0.008 # Scale to center at 0
# Calculate the Mean, Standard Deviation, and Standard Error for all samples
avgsim,sdsim = [],[]
n,i = 3,0
while i < len(sim1[' Y [ m ]']):
    e = np.array([sim1[' Velocity [ m s^-1 ]'][i],sim2[' Velocity [ m s^-1 ]'][i],sim3[' Velocity [ m s^-1 ]'][i]])
    avgsim.append(np.average(e))
    sdsim.append(np.std(e))
    i+=1
plussim = avgsim + 2*max(sdsim)/np.sqrt(n) # 2 standard deviations
minussim = avgsim - 2*max(sdsim)/np.sqrt(n) # 2 standard deviations
# -------------------------------------------------------------------
# EXPERIMENT SAMPLING
# --------------- 
expS1 = pd.read_csv("data/experiments/S1_Low_Exp_Outlet.csv") 
expS2 = pd.read_csv("data/experiments/S2_Low_Exp_Outlet.csv") 
expS3 = pd.read_csv("data/experiments/S3_Low_Exp_Outlet.csv") 
n = 3  # Number of Samples

# Calculate the Mean,Standard Deviation, Standard Error
avgexp,sdexp = [],[]
expS3nonoise = np.array(expS3['V (m/s)'][2:])
i = 0
while i < len(expS1['x (mm)']):
    e = np.array([expS1['V (m/s)'][i],expS2['V (m/s)'][i],expS3nonoise[i]])
    avgexp.append(np.average(e))
    sdexp.append(np.std(e))
    i+=1
plus = avgexp + 1*max(sdexp)/np.sqrt(n)
minus = avgexp - 1*max(sdexp)/np.sqrt(n)