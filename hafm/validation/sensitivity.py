import numpy as np
import math
import csv
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.size'] = 17
convert = 276.71 #273.15 #temp diff use -298.152039 

def srq_spatial_uncertainty(dataSimS1,dataSimS2):
    s1time = dataSimS1['Time [s]']
    s1TptInlet = dataSimS1['Monitor Point: Inlet (Temperature) [K]']-298.152039
    s1Tptneg05 = dataSimS1['Monitor Point: MouthpieceAbove1mmneg05Temp (Temperature) [K]']-298.152039
    s1Tpt0 = dataSimS1['Monitor Point: MouthpieceAbove1mm0mmTemp (Temperature) [K]']-298.152039
    s1Tpt0X05 = dataSimS1['Monitor Point: MouthpieceAbove1mm0mmX05mmT (Temperature) [K]']-298.152039
    s1Tpt05 = dataSimS1['Monitor Point: MouthpieceAbove1mm05mmTemp (Temperature) [K]']-298.152039
    s1Tpt1TRILINEAR = dataSimS1['Monitor Point: MouthpieceAbove1mm1mmTRILINEARTemp (Temperature) [K]']-298.152039
    s1Tpt1 = dataSimS1['Monitor Point: MouthpieceAbove1mm1mmTemp (Temperature) [K]']-298.152039
    s1Tpt1X05 = dataSimS1['Monitor Point: MouthpieceAbove1mm1mmX05mmT (Temperature) [K]']-298.152039
    s1Tpt15 = dataSimS1['Monitor Point: MouthpieceAbove1mm15mmTemp (Temperature) [K]']-298.152039
    s1Tpt2TRILINEAR = dataSimS1['Monitor Point: MouthpieceAbove1mm2mmTRILINEARTemp (Temperature) [K]']-298.152039
    s1Tpt2 = dataSimS1['Monitor Point: MouthpieceAbove1mm2mmTemp (Temperature) [K]']-298.152039
    s1Tpt2X05 = dataSimS1['Monitor Point: MouthpieceAbove1mm2mmX05mmT (Temperature) [K]']-298.152039
    s1Tpt25 = dataSimS1['Monitor Point: MouthpieceAbove1mm25mmTemp (Temperature) [K]']-298.152039
    s1Tpt3 = dataSimS1['Monitor Point: MouthpieceAbove1mm3mmTemp (Temperature) [K]']-298.152039
    s1Tpt3X05 = dataSimS1['Monitor Point: MouthpieceAbove1mm3mmX05mmT (Temperature) [K]']-298.152039
    s1Tpt35 = dataSimS1['Monitor Point: MouthpieceAbove1mm35mmTemp (Temperature) [K]']-298.152039
    s1Tpt4 = dataSimS1['Monitor Point: MouthpieceAbove1mm4mmTemp (Temperature) [K]']-298.152039
    s1Tpt4X05 = dataSimS1['Monitor Point: MouthpieceAbove1mm4mmX05mmT (Temperature) [K]']-298.152039
    # Tpt45 = dataSimS1['Monitor Point: MouthpieceAbove1mm45mmTemp (Absolute Pressure) [Pa]']
    s1Tpt5 = dataSimS1['Monitor Point: MouthpieceAbove1mm5mmTemp (Temperature) [K]']-298.152039

    s2time = dataSimS2['Time [s]']
    s2TptInlet = dataSimS2['Monitor Point: Inlet (Temperature) [K]']-298.152039
    s2Tptneg05 = dataSimS2['Monitor Point: MouthpieceAbove1mmneg05Temp (Temperature) [K]']-298.152039
    s2Tpt0 = dataSimS2['Monitor Point: MouthpieceAbove1mm0mmTemp (Temperature) [K]']-298.152039
    s2Tpt0X05 = dataSimS2['Monitor Point: MouthpieceAbove1mm0mmX05mmT (Temperature) [K]']-298.152039
    s2Tpt05 = dataSimS2['Monitor Point: MouthpieceAbove1mm05mmTemp (Temperature) [K]']-298.152039
    s2Tpt1TRILINEAR = dataSimS2['Monitor Point: MouthpieceAbove1mm1mmTRILINEARTemp (Temperature) [K]']-298.152039
    s2Tpt1 = dataSimS1['Monitor Point: MouthpieceAbove1mm1mmTemp (Temperature) [K]']-298.152039
    s2Tpt1X05 = dataSimS2['Monitor Point: MouthpieceAbove1mm1mmX05mmT (Temperature) [K]']-298.152039
    s2Tpt15 = dataSimS2['Monitor Point: MouthpieceAbove1mm15mmTemp (Temperature) [K]']-298.152039
    s2Tpt2TRILINEAR = dataSimS2['Monitor Point: MouthpieceAbove1mm2mmTRILINEARTemp (Temperature) [K]']-298.152039
    s2Tpt2 = dataSimS2['Monitor Point: MouthpieceAbove1mm2mmTemp (Temperature) [K]']-298.152039
    s2Tpt2X05 = dataSimS2['Monitor Point: MouthpieceAbove1mm2mmX05mmT (Temperature) [K]']-298.152039
    s2Tpt25 = dataSimS2['Monitor Point: MouthpieceAbove1mm25mmTemp (Temperature) [K]']-298.152039
    s2Tpt3 = dataSimS2['Monitor Point: MouthpieceAbove1mm3mmTemp (Temperature) [K]']-298.152039
    s2Tpt3X05 = dataSimS2['Monitor Point: MouthpieceAbove1mm3mmX05mmT (Temperature) [K]']-298.152039
    s2Tpt35 = dataSimS2['Monitor Point: MouthpieceAbove1mm35mmTemp (Temperature) [K]']-298.152039
    s2Tpt4 = dataSimS2['Monitor Point: MouthpieceAbove1mm4mmTemp (Temperature) [K]']-298.152039
    s2Tpt4X05 = dataSimS2['Monitor Point: MouthpieceAbove1mm4mmX05mmT (Temperature) [K]']-298.152039
    # Tpt45 = dataSimS1['Monitor Point: MouthpieceAbove1mm45mmTemp (Absolute Pressure) [Pa]']
    s2Tpt5 = dataSimS2['Monitor Point: MouthpieceAbove1mm5mmTemp (Temperature) [K]']-298.152039
    
    ## Plots
    plt.figure(figsize=(25,8))
    plt.subplot(1, 2, 1)
    plt.title('Diameter 1mm above mouthpiece') # \n Velocity=0.5147[m/s]')
    plt.xlabel('time [s]')
    plt.ylabel('Temperature Rise')
    # plt.plot(data_time[75:150]-19.5, average0,linestyle='-',label="ExpAverage_Center",color="black",linewidth=4)
    # # # plt.plot(data_time[75:150]-20, plus0,linestyle='-',color="gray",label="+2SD",)
    # # # plt.plot(data_time[75:150]-20, minus0,linestyle='-',color="gray",label="-2SD",)
    # plt.fill_between(data_time[75:150]-19.5,plus0, minus0, color="lightgray")
    # plt.plot(data_time[75:150]-19.5, average1,linestyle='-',label="ExpAverage_1mm",color="green",linewidth=4)
    # plt.fill_between(data_time[75:150]-19.5,plus1, minus1, color="lightgray")
    # plt.plot(data_time[75:150]-20, average2,linestyle='-',label="ExpAverage_2mm",color="blue",linewidth=4)
    # plt.fill_between(data_time[75:150]-19.5,plus2, minus2, color="lightgray")
    # plt.plot(data_time[75:150]-20, average4,linestyle='-',label="ExpAverage_4mm",color="darkgray",linewidth=4)
    # plt.fill_between(data_time[75:150]-19.5,plus4, minus4, color="lightgray")

    # plt.plot(s1time, s1TptInlet       , label='s1TptInlet       ') #,color="red",linewidth=4    
    # plt.plot(s1time, s1Tptneg05       , label='radius=-0.5      ') #,color="red",linewidth=4    
    plt.plot(s1time, s1Tpt0           , label='radius=0         ',color="green") #,color="red",linewidth=4 
    plt.plot(s1time, s1Tpt0X05        , label='radius=0,x=0.5   ',linestyle="dotted",color="green") #,color="red",linewidth=4   
    # plt.plot(s1time, s1Tpt05          , label='radius=0.5          ') #,color="red",linewidth=4 
    plt.plot(s1time, s1Tpt1TRILINEAR  , label='radius=1(Interpolation)  ',color='blue') #,color="red",linewidth=4         
    # plt.plot(s1time, s1Tpt1           , label='radius=1           ') #,color="red",linewidth=4
    plt.plot(s1time, s1Tpt1X05        , label='radius=1,x=0.5        ',linestyle="dotted",color='blue') #,color="red",linewidth=4   
    # plt.plot(s1time, s1Tpt15          , label='radius=1.5          ') #,color="red",linewidth=4 
    plt.plot(s1time, s1Tpt2TRILINEAR  , label='radius=2(Interpolation)  ',color="magenta") #,color="red",linewidth=4         
    # plt.plot(s1time, s1Tpt2           , label='radius=2           ') #,color="red",linewidth=4
    plt.plot(s1time, s1Tpt2X05        , label='radius=2,x=0.5        ',linestyle="dotted",color="magenta") #,color="red",linewidth=4   
    # plt.plot(s1time, s1Tpt25          , label='radius=2.5          ') #,color="red",linewidth=4 
    plt.plot(s1time, s1Tpt3           , label='radius=3           ',color="cyan") #,color="red",linewidth=4
    plt.plot(s1time, s1Tpt3X05        , label='radius=3,x=0.5        ',linestyle="dotted",color="cyan" ) #,color="red",linewidth=4   
    # plt.plot(s1time, s1Tpt35          , label='radius=3.5          ') #,color="red",linewidth=4 
    plt.plot(s1time, s1Tpt4           , label='radius=4           ',color='red') #,color="red",linewidth=4
    plt.plot(s1time, s1Tpt4X05        , label='radius=4,x=0.5        ',linestyle="dotted",color='red') #,color="red",linewidth=4   
    # plt.plot(s1time, s1Tpt5           , label='radius=5           ') #,color="red",linewidth=4

    # plt.xlim([-0.5,18])
    # plt.ylim([-0.1, 3.5])
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.savefig('figures/srq_outputUncertainty05x.png', bbox_inches='tight', dpi=300)
    plt.grid()
    return
####-----------------------------------------------------------------
##----------------- SRQ Output Uncertainties Point 0
####-----------------------------------------------------------------
def srq_outputUncertainty_pt0(headerLabels,dataSample1,dataSample2,dataSample3,dataSample4,dataSample5,dataSample6,dataSample7,dataSample8,dataSample9,dataSample10):
    #### All Uncertainties
    plt.figure(figsize=(12,8))
    # Z 1mm above mouthpiece
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample1')
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample2')
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample3')
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample4')
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample5')
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample6')
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample7')
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample8')
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample9')
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm0mmTempXdownYZ (Temperature) [K]']-convert, label='Sample10')

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm0mmTempXupYZ (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm0mmTempX0YZ (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm0mmTempX0YupZ (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm0mmTempX0YdownZ (Temperature) [K]']-convert)

    ##### Z up
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp0mmTempzXdownYZ (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp0mmTempzXupYZup (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp0mmTempzX0YZup (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp0mmTempzX0YupZup (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp0mmTempzX0YdownZup (Temperature) [K]']-convert)

    ## Z down
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown0mmTempzXdownYZ (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown0mmTempzXupYZdown (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown0mmTempzX0YZdown (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown0mmTempzX0YupZdown (Temperature) [K]']-convert)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown0mmTempzX0YdownZdown (Temperature) [K]']-convert)

#     plt.plot(data_time[75:150]-19.65, average0,linestyle='-',label="Experiments&1SD",color="black")
    # plt.fill_between(data_time[75:150]-19.650,erravgplus0, erravgminus0, color="lightgreen")
#     plt.fill_between(data_time[75:150]-19.65,plus0, minus0, color="lightgray")

    plt.grid()
    plt.xlim([-0.5,12])
    # plt.ylim([-0.25,5])
    plt.title('Point 0 - All Output Uncertainties');
    plt.xlabel('time [s]')
    plt.ylabel('Temperature Rise')
    plt.legend(bbox_to_anchor=(1.02, 1.0), loc='upper left', borderaxespad=0);
    plt.savefig('figures/srq_outputUncertainty_point0.png', dpi=300)
    return 
####-----------------------------------------------------------------
##----------------- SRQ Output Uncertainties Point 1
####-----------------------------------------------------------------
def srq_outputUncertainty_pt1(headerLabels,dataSample1,dataSample2,dataSample3,dataSample4,dataSample5,dataSample6,dataSample7,dataSample8,dataSample9,dataSample10):    
    #### All Uncertainties
    plt.figure(figsize=(12,8))
    # Z 1mm above mouthpiece
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample1')
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample2')
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample3')
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample4')
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample5')
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample6')
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample7')
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample8')
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample9')
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm1mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample10')

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm1mmTempXupYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm1mmTempX0YZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm1mmTempX0YupZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm1mmTempX0YdownZ (Temperature) [K]']-298.152039)

    ##### Z up
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp1mmTempzXdownZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp1mmTempzXupYZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp1mmTempzX0YZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp1mmTempzX0YupZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp1mmTempzX0YdownZup (Temperature) [K]']-298.152039)

    ## Z down
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown1mmTempzXdownYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown1mmTempzXupYZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown1mmTempzX0YZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown1mmTempzX0YupZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown1mmTempzX0YdownZdown (Temperature) [K]']-298.152039)

#     plt.plot(data_time[75:150]-19.65, average1,linestyle='-',label="Experiments&1SD",color="black")
#     # plt.fill_between(data_time[75:150]-19.650,erravgplus0, erravgminus0, color="lightgreen")
#     plt.fill_between(data_time[75:150]-19.65,plus1, minus1, color="lightgray")

    plt.grid()
    plt.xlim([-0.5,12])
    # plt.ylim([-0.25,5])
    plt.title('Point 1 - All Output Uncertainties');
    plt.xlabel('time [s]')
    plt.ylabel('Temperature Rise')
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);
    plt.savefig('figures/srq_outputUncertainty_point1.png', dpi=300)
    return
####-----------------------------------------------------------------
##----------------- SRQ Output Uncertainties Point 2
####-----------------------------------------------------------------
def srq_outputUncertainty_pt2(headerLabels,dataSample1,dataSample2,dataSample3,dataSample4,dataSample5,dataSample6,dataSample7,dataSample8,dataSample9,dataSample10):
    #### All Uncertainties
    plt.figure(figsize=(12,8))
    # Z 1mm above mouthpiece
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample1')
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample2')
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample3')
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample4')
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample5')
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample6')
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample7')
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample8')
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample9')
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm2mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample10')

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm2mmTempXupYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm2mmTempX0YZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm2mmTempX0YupZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm2mmTempX0YdownZ (Temperature) [K]']-298.152039)

    ##### Z up
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp2mmTempzXdownYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp2mmTempzXupYZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp2mmTempzX0YZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp2mmTempzX0YupZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp2mmTempzX0YdownZup (Temperature) [K]']-298.152039)

    ## Z down
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown2mmTempzXdownYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown2mmTempzXupYZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown2mmTempzX0YZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown2mmTempzX0YupZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown2mmTempzX0YdownZdpwm (Temperature) [K]']-298.152039)

#     plt.plot(data_time[75:150]-19.65, average2,linestyle='-',label="Experiments&1SD",color="black")
#     # plt.fill_between(data_time[75:150]-19.650,erravgplus0, erravgminus0, color="lightgreen")
#     plt.fill_between(data_time[75:150]-19.65,plus2, minus2, color="lightgray")

    # plt.plot(data_time[75:150]-19.65, average4,linestyle='-',label="ExpAverage_Center",color="black")
    # # plt.fill_between(data_time[75:150]-19.650,erravgplus0, erravgminus0, color="lightgreen")
    # plt.fill_between(data_time[75:150]-19.65,plus4, minus4, color="lightgray")
    plt.grid()
    plt.xlim([-0.5,12])
    # plt.ylim([-0.25,5])
    plt.title('Point 2 - All Output Uncertainties');
    plt.xlabel('time [s]')
    plt.ylabel('Temperature Rise')
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);
    plt.savefig('figures/srq_outputUncertainty_point2.png', dpi=300)
    return
####-----------------------------------------------------------------
##----------------- SRQ Output Uncertainties Point 3
####-----------------------------------------------------------------
def srq_outputUncertainty_pt3(headerLabels,dataSample1,dataSample2,dataSample3,dataSample4,dataSample5,dataSample6,dataSample7,dataSample8,dataSample9,dataSample10):
    #### All Uncertainties
    plt.figure(figsize=(12,8))
    # Z 1mm above mouthpiece
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample1')
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample2')
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample3')
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample4')
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample5')
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample6')
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample7')
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample8')
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample9')
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm3mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample10')

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm3mmTempXupYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm3mmTempX0YZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm3mmTempX0YupZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm3mmTempX0YdownZ (Temperature) [K]']-298.152039)

    ##### Z up
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp3mmTempzXdownYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp3mmTempzXupYZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp3mmTempzX0YZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp3mmTempzX0YupZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp3mmTempzX0YdownZup (Temperature) [K]']-298.152039)

    ## Z down
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown3mmTempzXdownYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown3mmTempzXupYZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown3mmTempzX0YZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown3mmTempzX0YupZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown3mmTempzX0YdownZdown (Temperature) [K]']-298.152039)

    plt.grid()
    plt.xlabel('time [s]')
    plt.ylabel('Temperature Rise')
    plt.xlim([-0.5,12])
    # plt.ylim([-0.25,5])
    plt.title('Point 3 - All Output Uncertainties');
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);
    plt.savefig('figures/srq_outputUncertainty_point3.png.png', dpi=300)
    return
####-----------------------------------------------------------------
##----------------- SRQ Output Uncertainties Point 4
####-----------------------------------------------------------------
def srq_outputUncertainty_pt4(headerLabels,dataSample1,dataSample2,dataSample3,dataSample4,dataSample5,dataSample6,dataSample7,dataSample8,dataSample9,dataSample10):
    #### All Uncertainties
    plt.figure(figsize=(12,8))
    # Z 1mm above mouthpiece
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample1')
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample2')
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample3')
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample4')
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample5')
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample6')
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample7')
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample8')
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample9')
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm4mmTempXdownYZ (Temperature) [K]']-298.152039, label='Sample10')

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm4mmTempXupYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm4mmTempX0YZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm4mmTempX0YupZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: Mouthpiece1mm4mmTempX0YdownZ (Temperature) [K]']-298.152039)

    ##### Z up
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp4mmTempXdownYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp4mmTempXupYZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp4mmTempX0YZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp4mmTempX0YupZup (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceUp4mmTempX0YdownZup (Temperature) [K]']-298.152039)

    ## Z down
    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown4mmTempzXdownYZ (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown4mmTempzXupYZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown4mmTempzX0YZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown4mmTempzX0YupZdown (Temperature) [K]']-298.152039)

    plt.plot(dataSample1[headerLabels[0]],dataSample1['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample2[headerLabels[0]],dataSample2['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample3[headerLabels[0]],dataSample3['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample4[headerLabels[0]],dataSample4['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample5[headerLabels[0]],dataSample5['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample6[headerLabels[0]],dataSample6['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample7[headerLabels[0]],dataSample7['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample8[headerLabels[0]],dataSample8['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample9[headerLabels[0]],dataSample9['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)
    plt.plot(dataSample10[headerLabels[0]],dataSample10['Monitor Point: MouthpieceDown4mmTempzX0YdownZdown (Temperature) [K]']-298.152039)

#     plt.plot(data_time[75:150]-19.65, average4,linestyle='-',label="Experiment&1SD",color="black")
#     # plt.fill_between(data_time[75:150]-19.650,erravgplus0, erravgminus0, color="lightgreen")
#     plt.fill_between(data_time[75:150]-19.65,plus4, minus4, color="lightgray")
    plt.grid()
    plt.xlabel('time [s]')
    plt.ylabel('Temperature Rise')
    plt.xlim([-0.5,12])
    # plt.ylim([-0.25,5])
    plt.title('Point 4 - All Output Uncertainties');
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);
    plt.savefig('figures/srq_outputUncertainty_point4.png', dpi=300)
    return
    