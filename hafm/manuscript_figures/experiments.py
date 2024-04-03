import pandas as pd
import numpy as np

### Experiments: Raw Data - Temp Diff
# t=sample,T=radial position,T1:2mm,T2:r=0mm (Center),T3:r=1mm,T4:r=4mm 
tempEdiff = pd.read_csv('data/Temp_Diff_Data/exp_1W_0.5LPM.csv')  # Power=1 Watt, Volumetric Airflow=0.5 L/min
# tempEdiff = pd.read_csv('data/Temp_Diff_Data/Exp_1W_1.65LPM.csv') # Power 1 Watt, VFR=1.65 L/min
timeEdiff   = tempEdiff['Time']
tempET1diff = [tempEdiff['T1_t1'],tempEdiff['T1_t2'],tempEdiff['T1_t3']]
tempET2diff = [tempEdiff['T2_t1'],tempEdiff['T2_t2'],tempEdiff['T2_t3']]
tempET3diff = [tempEdiff['T3_t1'],tempEdiff['T3_t2'],tempEdiff['T3_t3']]
tempET4diff = [tempEdiff['T4_t1'],tempEdiff['T4_t2'],tempEdiff['T4_t3']]
### Experiments: Raw Data 
# T(Sample) T(radial position) 
tempE = pd.read_csv('data/Raw_Temp_Data/Air_Temperature_Measurements_1W_0.5LPM.csv')
timeE = tempE['Time']
tempET1 = [tempE['T1T1'],tempE['T2T1'],tempE['T3T1']]
tempET2 = [tempE['T1T2'],tempE['T2T2'],tempE['T3T2']]
tempET3 = [tempE['T1T3'],tempE['T2T3'],tempE['T3T3']]
tempET4 = [tempE['T1T4'],tempE['T2T4'],tempE['T3T4']]
tempE.tail()
#---------------------------------------------------------------
### Experiment Metrics: mean & standard deviation over 3 samples
i = 75 # Start here because there are a lot of power off values. 
avg0,avg1,avg2,avg4 = [],[],[],[]
sd0,sd1,sd2,sd4 = [],[],[],[]
while i < 150:
    a4 = [tempET4[0][i],tempET4[1][i],tempET4[2][i]] #4mm
    a2 = [tempET1[0][i],tempET1[1][i],tempET1[2][i]] #2mm
    a1 = [tempET3[0][i],tempET3[1][i],tempET3[2][i]] #1mm     
    a0 = [tempET2[0][i],tempET2[1][i],tempET2[2][i]] #center
    avg0.append(np.average(a0))
    avg1.append(np.average(a1))
    avg2.append(np.average(a2))
    avg4.append(np.average(a4))
    sd0.append(np.std(a0))
    sd1.append(np.std(a1))
    sd2.append(np.std(a2))
    sd4.append(np.std(a4))
    i +=1
# Take the largest standard deviation and apply that across all means 
# Key: u=upper bound, l=lower bound
u0=avg0 + 1*max(sd0) #/len(a0) # 3 samples
u1=avg1 + 1*max(sd1) #/len(a0) # 3 samples
u2=avg2 + 1*max(sd2) #/len(a0) # 3 samples
u4=avg4 + 1*max(sd4) #/len(a0) # 3 samples
l0=avg0 - 1*max(sd0) #/len(a0) # 3 samples
l1=avg1 - 1*max(sd1) #/len(a0) # 3 samples
l2=avg2 - 1*max(sd2) #/len(a0) # 3 samples
l4=avg4 - 1*max(sd4) #/len(a0) # 3 samples

exp_avg = {'time': timeE, 'avg_r0': avg0, 'avg_r1': avg1,'avg_r2': avg2,'avg_r4': avg4,}   