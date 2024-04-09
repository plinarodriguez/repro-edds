# Libraries
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Set the font family and size to use for Matplotlib figures.
plt.rcParams['font.size'] = 17
#-------------------------------------
# Geometry
labels = ['Mouthpiece','Pipe','Atomizer','Inlet Pipe']
diam = [8.02,4.54,4.54,4.54]
length = [13.96,27.955,7.5,2.17]
thick = [0.13,0.15,0.15,0.15]
geom_db = pd.DataFrame({'label':labels,'Diameter[mm]':diam,'Length[mm]':length,'Thickness[mm]':thick})
coil10 = {'Coil_qty':12,'Coil_Diameter':0.3,'Coil_Spacing':0.5} #label,qty,outter diameter,single coil diameter,space btw coils
#----------------------------------
# Conversions
def vel_power(vfr,powerraw):
    vfr_m3sec = vfr / (6*10**4)           # m^3/sec
    diameter = 4.54                 # inlet diameter [mm]
    diameterm = diameter/(10**3)    # inlet diameter [m]
    radius = diameterm/2 
    vel = vfr_m3sec /(math.pi*(radius**2)) #velocity [m/s]
    power = (powerraw/13.1533)*(10**9 /1)  #power/volume [W/m^3]
    return(vel,power)
## Input Uncertainties
def inputUncert(vfr,powerraw,timeToMaxPower):
    vel,power = vel_power(vfr,powerraw)
    sampleID = ['sample 1','sample 2','sample 3','sample 4','sample 5','sample 6','sample 7','sample 8','sample 9','sample 10']
    samples = pd.DataFrame( {'Sample':sampleID,'VFR (L/min)': vfr,'Velocity [m/s]': vel, 'Power [W]':powerraw, 'Power/volume [W/m^3]': power,'Time to Max Power [sec]': timeToMaxPower})
    return samples

# Power Profiles and SRQ locations
def powerprof(dataPowerS1,dataPowerS2,dataPowerS3,dataPowerS4,dataPowerS5,dataPowerS6,dataPowerS7,dataPowerS8,dataPowerS9,dataPowerS10, save):
    plt.figure(figsize=(14,8))
    plt.title('Applied Power Profiles')
    plt.xlabel('Time [s]')
    plt.ylabel('Power [W]')
    plt.plot(dataPowerS1['t[s]'], dataPowerS1['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample1') 
    plt.plot(dataPowerS2['t[s]'], dataPowerS2['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample2') 
    plt.plot(dataPowerS3['t[s]'], dataPowerS3['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample3') 
    plt.plot(dataPowerS4['t[s]'], dataPowerS4['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample4') 
    plt.plot(dataPowerS5['t[s]'], dataPowerS5['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample5')
    plt.plot(dataPowerS6['t[s]'], dataPowerS6['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample6') 
    plt.plot(dataPowerS7['t[s]'], dataPowerS7['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample7') 
    plt.plot(dataPowerS8['t[s]'], dataPowerS8['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample8') 
    plt.plot(dataPowerS9['t[s]'], dataPowerS9['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample9') 
    plt.plot(dataPowerS10['t[s]'], dataPowerS10['Power[W m^-3]']/((1/13.1533)*(1e9)),label='Sample10') 
    plt.scatter([0,2,5,10,11,12],[0,1,1,1,0.5,0], marker='x', color='black',s=300, lw=5)
    plt.grid()
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    if save == 'YES' :
        plt.savefig('figures/appliedPowerProfiles_samples10.png', dpi=300, bbox_inches='tight');

###### Convert .out to .dat
def convertDat(input_file,output_file,label):
    # Initialize an empty list to store the sample data
    sample_data = []

    # Open the .out file for reading
    with open(input_file, 'r') as infile:
        # Flag to indicate if @SAMPLEDATA section has been reached
        read_sample_data = False

        # Iterate through each line in the .out file
        for line in infile:
            # Check if @SAMPLEDATA section has been reached
            if '@SAMPLEDATA' in line:
                read_sample_data = True
                continue  # Skip the line with '@SAMPLEDATA'

            # If @SAMPLEDATA section has been reached, read the data
            if read_sample_data:
                # Split the line into fields and extract the relevant data
                fields = line.strip().split()
                sample_data.append(fields[2:])  # Skip the first two fields (sample index and number of observations)

    # Write the sample data to the output .dat file
    with open(output_file, 'w') as outfile:
        # Write a header line
#         outfile.write('VFR Power\n')
        outfile.write(label+'\n')

        # Write each row of sample data to the file
        for row in sample_data:
            outfile.write(' '.join(row) + '\n')
    return