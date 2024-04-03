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