import pandas as pd
import numpy as np

# Simulation Sample 
tempS1 = pd.read_csv("Data/data_sim/outputSample1.csv",skiprows = 4)
tempS2 = pd.read_csv("Data/data_sim/outputSample2.csv",skiprows = 4)
tempS3 = pd.read_csv("Data/data_sim/outputSample3.csv",skiprows = 4)
tempS4 = pd.read_csv("Data/data_sim/outputSample4.csv",skiprows = 4)
tempS5 = pd.read_csv("Data/data_sim/outputSample5.csv",skiprows = 4)
tempS6 = pd.read_csv("Data/data_sim/outputSample6.csv",skiprows = 4)
tempS7 = pd.read_csv("Data/data_sim/outputSample7.csv",skiprows = 4)
tempS8 = pd.read_csv("Data/data_sim/outputSample8.csv",skiprows = 4)
tempS9 = pd.read_csv("Data/data_sim/outputSample9.csv",skiprows = 4)
tempS10 = pd.read_csv("Data/data_sim/outputSample10.csv",skiprows = 4)
tempSLab = tempS1.columns # header labels

## Create a Dataframe for a Quantative Max Temperaure with uncertainties for 4 radial positions
i,s,uq = 1,1,[]
tempS1Max,tempS2Max,tempS3Max,tempS4Max,tempS5Max = [],[],[],[],[]
tempS6Max,tempS7Max,tempS8Max,tempS9Max,tempS10Max = [],[],[],[],[]
while i < len(tempSLab):
    tempS1Max.append( np.max(tempS1 [tempSLab[i]]))
    tempS2Max.append( np.max(tempS2 [tempSLab[i]]))
    tempS3Max.append( np.max(tempS3 [tempSLab[i]]))
    tempS4Max.append( np.max(tempS4 [tempSLab[i]]))
    tempS5Max.append( np.max(tempS5 [tempSLab[i]]))
    tempS6Max.append( np.max(tempS6 [tempSLab[i]]))
    tempS7Max.append( np.max(tempS7 [tempSLab[i]]))
    tempS8Max.append( np.max(tempS8 [tempSLab[i]]))
    tempS9Max.append( np.max(tempS9 [tempSLab[i]]))
    tempS10Max.append(np.max(tempS10[tempSLab[i]]))
    i+=1;
tempMax =pd.DataFrame([tempS1Max,tempS2Max,tempS3Max,tempS4Max,tempS5Max,
         tempS6Max,tempS7Max,tempS8Max,tempS9Max,tempS10Max])
tempMax.columns = tempSLab[1:]
while s < len(tempSLab):
    x = np.mean(tempMax[tempSLab[s]])
    y = np.std(tempMax[tempSLab[s]])
    x = round(x,5 - len(str(int(x))))
    y = round(y,5 - len(str(int(y))))              
    x = str(x)
    y = str(y)
    uq.append(x + '+/- '+ y)
    s+=1;
maxUQ = pd.DataFrame(uq)
maxUQtrans = maxUQ.transpose()
maxUQtrans.columns = tempSLab[1:]
maxUQ_radial= pd.DataFrame([maxUQtrans['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]'],
maxUQtrans['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]'],
maxUQtrans['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]'],
maxUQtrans['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]'],
maxUQtrans['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']],
             ['r=0mm','r=1mm','r=2mm','r=3mm','r=4mm'])

#----------------------------------------
# Simulation Data by timestep
# ----------------------------
### These are the means
def simMeans_bytime(timesteps,timeEId):
    headers = tempS1.columns
    times = pd.DataFrame([tempS1[headers[0]],tempS2[headers[0]],tempS3[headers[0]],tempS4[headers[0]],tempS5[headers[0]],tempS6[headers[0]],tempS7[headers[0]],tempS8[headers[0]],tempS9[headers[0]],tempS10[headers[0]]])                                                                         
    time_list = [tempS1[headers[0]]]
    time_list = list(time_list[0][0:])
    avgTS_ts0 = [meanSamplesP0[timesId[0]],meanSamplesP1[timesId[0]],meanSamplesP2[timesId[0]],meanSamplesP4[timesId[0]]]
    sdTS_ts0 = [stdSamplesP0[timesId[0]],stdSamplesP1[timesId[0]],stdSamplesP2[timesId[0]],stdSamplesP4[timesId[0]]]
    # timestep =  2  
    avgTS_ts2 = [meanSamplesP0[timesId[2]],meanSamplesP1[timesId[2]],meanSamplesP2[timesId[2]],meanSamplesP4[timesId[2]]]
    sdTS_ts2 = [stdSamplesP0[timesId[2]],stdSamplesP1[timesId[2]],stdSamplesP2[timesId[2]],stdSamplesP4[timesId[2]]]
    # timestep =  5  
    avgTS_ts4 = [meanSamplesP0[timesId[4]],meanSamplesP1[timesId[4]],meanSamplesP2[timesId[4]],meanSamplesP4[timesId[4]]]
    sdTS_ts4 = [stdSamplesP0[timesId[4]],stdSamplesP1[timesId[4]],stdSamplesP2[timesId[4]],stdSamplesP4[timesId[4]]]
    # timestep =  10  
    avgTS_ts5 = [meanSamplesP0[timesId[5]],meanSamplesP1[timesId[5]],meanSamplesP2[timesId[5]],meanSamplesP4[timesId[5]]]
    sdTS_ts5 = [stdSamplesP0[timesId[5]],stdSamplesP1[timesId[5]],stdSamplesP2[timesId[5]],stdSamplesP4[timesId[5]]]
    # timestep =  11  
    avgTS_ts6 = [meanSamplesP0[timesId[6]],meanSamplesP1[timesId[6]],meanSamplesP2[timesId[6]],meanSamplesP4[timesId[6]]]
    sdTS_ts6 = [stdSamplesP0[timesId[6]],stdSamplesP1[timesId[6]],stdSamplesP2[timesId[6]],stdSamplesP4[timesId[6]]]
    # timestep =  12  
    avgTS_ts7 = [meanSamplesP0[timesId[7]],meanSamplesP1[timesId[7]],meanSamplesP2[timesId[7]],meanSamplesP4[timesId[7]]]
    sdTS_ts7 = [stdSamplesP0[timesId[7]],stdSamplesP1[timesId[7]],stdSamplesP2[timesId[7]],stdSamplesP4[timesId[7]]]
    timesId = [time_list.index(0.00999999978),time_list.index(timesteps[1]),time_list.index(timesteps[2]),time_list.index(timesteps[3]),time_list.index(timesteps[4]),time_list.index(timesteps[5]),
               time_list.index(timesteps[6]),time_list.index(timesteps[7])]
    avg_ts_S, sd_ts_S = [], []
    i = 0
    while i < len(timeEId):
        avg_ts_S.append([avg0[timeEId[i]],avg1[timeEId[i]],avg2[timeEId[i]],avg4[timeEId[i]]])
        sd_ts_S.append([sd0[timeEId[i]],sd1[timeEId[i]],sd2[timeEId[i]],sd4[timeEId[i]]])
        i+=1
    