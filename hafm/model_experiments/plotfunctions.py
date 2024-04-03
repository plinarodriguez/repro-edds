from matplotlib import pyplot
import numpy as np

# Power Profiles and SRQ locations
def powerprof(dataPowerS1,dataPowerS2,dataPowerS3,dataPowerS4,dataPowerS5,dataPowerS6,dataPowerS7,dataPowerS8,dataPowerS9,dataPowerS10, save):
    pyplot.figure(figsize=(14,8))
    pyplot.title('Applied Power Profiles')
    pyplot.xlabel('Time [s]')
    pyplot.ylabel('Power [W]')
    pyplot.plot(dataPowerS1['t[s]'], dataPowerS1['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample1') 
    pyplot.plot(dataPowerS2['t[s]'], dataPowerS2['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample2') 
    pyplot.plot(dataPowerS3['t[s]'], dataPowerS3['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample3') 
    pyplot.plot(dataPowerS4['t[s]'], dataPowerS4['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample4') 
    pyplot.plot(dataPowerS5['t[s]'], dataPowerS5['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample5')
    pyplot.plot(dataPowerS6['t[s]'], dataPowerS6['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample6') 
    pyplot.plot(dataPowerS7['t[s]'], dataPowerS7['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample7') 
    pyplot.plot(dataPowerS8['t[s]'], dataPowerS8['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample8') 
    pyplot.plot(dataPowerS9['t[s]'], dataPowerS9['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample9') 
    pyplot.plot(dataPowerS10['t[s]'], dataPowerS10['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample10') 
    pyplot.scatter([0,2,5,10,11,12],[0,1,1,1,0.5,0], marker='x', color='black',s=300, lw=5)
    pyplot.grid()
    pyplot.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    if save == 'YES' :
        pyplot.savefig('figures/appliedPowerProfiles_samples10.png', dpi=300, bbox_inches='tight');
   
# Plot function to repeat
def sampleplotslabels(point,tempS1,tempS2,tempS3,tempS4,tempS5,tempS6,tempS7,tempS8,tempS9,tempS10,tempSLab):
    samples = [tempS1,tempS2,tempS3,tempS4,tempS5,tempS6,tempS7,tempS8,tempS9,tempS10]
    nameSample = ['Sample1','Sample2','Sample3','Sample4','Sample5','Sample6','Sample7','Sample8','Sample9','Sample10']
    i = 0
    for sample in samples:
        pyplot.plot(sample[tempSLab[0]], sample[point]-298.152039, label=nameSample[i])
        i+=1
    
# Plots Simulation vs. Experiments - by Point Location - Diamter ONLY
def sim_exp_pointlabels(timeE,avg,u,l,tempS1,tempS2,tempS3,tempS4,tempS5,
                  tempS6,tempS7,tempS8,tempS9,tempS10,
                  tempSLab,r,point,save,plotexp):
    pyplot.figure(figsize=(12,8))
    pyplot.xlabel('time [s]')
    pyplot.ylabel('Temperature Rise')
    sampleplotslabels(point,tempS1,tempS2,tempS3,tempS4,tempS5,tempS6,tempS7,tempS8,tempS9,tempS10,tempSLab)
    if plotexp == 'YES':
        pyplot.plot(timeE[75:150]-19.650, avg,linestyle='-',label="Experiment",color="black")
        pyplot.fill_between(timeE[75:150]-19.650,u,l, color="lightgray")
    pyplot.grid()
    pyplot.xlim([-0.5,12])
    pyplot.title('Simulations (radius='+str(r)+'mm)')
#     pyplot.title('r='+ str(r)+'mm');
    pyplot.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0);
    if save == 'YES' :
        if plotexp == 'YES':
            pyplot.savefig('figures/simulation_exp_radius%imm.png'%r, dpi=300, bbox_inches='tight') 
        else: 
            pyplot.savefig('figures/simulation_radius%imm.png'%r, dpi=300, bbox_inches='tight')
            
             
# Experimental data plots by raw data vs. mean & SD
def exp_statsvsraw_2plots(radius, time, average,upperbound,lowerbound,rawdata,save): 
    r = str(radius) 
    pyplot.figure(figsize=(20,7)) 
    pyplot.subplot(1, 2, 1) 
    pyplot.title('Experiments (radius='+r+'mm)') 
    pyplot.xlabel('time [s]') 
    pyplot.ylabel('Temperature Rise') 
    pyplot.plot( time[75:150]-20,average,linestyle='-',color= "black",label= "Mean") 
    pyplot.plot( time[75:150]-20,upperbound,linestyle='-',color= "gray",label= "SD" ) 
    pyplot.plot( time[75:150]-20,lowerbound,linestyle='-',color= "gray") 
    pyplot.fill_between( time[75:150]-20, upperbound,lowerbound, color= "lightgray") 
    pyplot.legend()
    pyplot.grid() 
    pyplot.xlim(-0.1,15) 
    pyplot.subplot(1, 2, 2) 
    pyplot.plot( time[75:150]-20, average,linestyle='-',label= "Mean ",color= "black") 
    pyplot.scatter( time[75:150]-20, np.abs(rawdata[0])[75:150],label= "Sample_1") 
    pyplot.scatter( time[75:150]-20, np.abs(rawdata[1])[75:150],label= "Sample_2") 
    pyplot.scatter( time[75:150]-20, np.abs(rawdata[2])[75:150],label= "Sample_3") 
    pyplot.legend()
    pyplot.grid()
    pyplot.xlim(-0.1,15)
    if save == 'YES' :
        pyplot.savefig('figures/experiments_radius'+r+'mm.png', dpi=300, bbox_inches='tight'); 
    return;
# All Experimental Data
def exp_ALL_2plots(timeE,avg0,avg1,avg2,avg4,
                   u0,u1,u2,u4,
                   l0,l1,l2,l4,
                   tempET1,tempET2,tempET3,tempET4,save):
    pyplot.figure(figsize=(20,7))
    pyplot.subplot(1, 2, 1)
    pyplot.title('Experiments')
    pyplot.xlabel('time [s]')
    pyplot.ylabel('Temperature Rise')
    pyplot.plot(timeE[75:150]-20, avg0,linestyle='dashdot',label="r=0",color="black",linewidth=4)
    pyplot.plot(timeE[75:150]-20, u0,linestyle='-',color="gray")
    pyplot.plot(timeE[75:150]-20, l0,linestyle='-',color="gray")
    pyplot.fill_between(timeE[75:150]-20,u0, l0, color="lightgray")

    pyplot.plot(timeE[75:150]-20, avg1,linestyle='dashed',label="r=1",color="black",linewidth=4)
    pyplot.plot(timeE[75:150]-20, u1,linestyle='-',color="gray")
    pyplot.plot(timeE[75:150]-20, l1,linestyle='-',color="gray")
    pyplot.fill_between(timeE[75:150]-20,u1, l1, color="lightgray")

    pyplot.plot(timeE[75:150]-20, avg2,linestyle='-',label="r=2",color="black",linewidth=4)
    pyplot.plot(timeE[75:150]-20, u2,linestyle='-',color="gray")
    pyplot.plot(timeE[75:150]-20, l2,linestyle='-',color="gray")
    pyplot.fill_between(timeE[75:150]-20,u2, l2, color="lightgray")

    pyplot.plot(timeE[75:150]-20, avg4,linestyle='dotted',label="r=4",color="black",linewidth=4)
    pyplot.plot(timeE[75:150]-20, u4,linestyle='-',color="gray")
    pyplot.plot(timeE[75:150]-20, l4,linestyle='-',label="1SD",color="gray")
    pyplot.fill_between(timeE[75:150]-20,u4, l4, color="lightgray")

    pyplot.legend()
    pyplot.grid()
    pyplot.xlim(-0.1,15)
    pyplot.subplot(1, 2, 2)

    pyplot.scatter(timeE[75:150]-20, np.abs(tempET2[0])[75:150],label="Sample_1", color='royalblue')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET2[1])[75:150],label="Sample_2", color='darkorange')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET2[2])[75:150],label="Sample_3", color='mediumseagreen')
    pyplot.plot(timeE[75:150]-20, avg0,linestyle='dashdot',color="black",linewidth=4)

    pyplot.scatter(timeE[75:150]-20, np.abs(tempET3[0])[75:150], color='royalblue')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET3[1])[75:150], color='darkorange')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET3[2])[75:150], color='mediumseagreen')
    pyplot.plot(timeE[75:150]-20, avg1,linestyle='dashed',color="black",linewidth=4)

    pyplot.scatter(timeE[75:150]-20, np.abs(tempET1[0])[75:150], color='royalblue')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET1[1])[75:150], color='darkorange')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET1[2])[75:150], color='mediumseagreen')
    pyplot.plot(timeE[75:150]-20, avg2,linestyle='-',color="black",linewidth=4)

    pyplot.scatter(timeE[75:150]-20, np.abs(tempET4[0])[75:150], color='royalblue')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET4[1])[75:150], color='darkorange')
    pyplot.scatter(timeE[75:150]-20, np.abs(tempET4[2])[75:150], color='mediumseagreen')
    pyplot.plot(timeE[75:150]-20, avg4,linestyle='dotted',color="black",linewidth=4)

    pyplot.legend();
    pyplot.grid();
    pyplot.xlim(-0.1,15);
    if save == 'YES' :
        pyplot.savefig('figures/experiments_radiusALL.png', dpi=300, bbox_inches='tight');        
        