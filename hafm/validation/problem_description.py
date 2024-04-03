# Libraries
import pandas as pd
import numpy as np
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
# LHS Sampling - Input Uncertainties for Simulation
velocity = ['VFR [L/min]',0.49443986342754215,0.49727473790757359,0.50662655679974711,0.50958889995235945,0.49179642068222162,0.49413438308052721,0.50741464606951925,0.50837221808731559,0.49976822379976510,0.49110360241495071]
power = ['Power[W]',0.99985413804277778,1.0002659078601281,0.99979680049582387,1.0004908209322021,1.0003082816863897,0.99989673660648992,1.0000184179912321,0.99968772122613159,1.0001117438615765,0.99998663799837229]
powerOnOff = ['Time to Max Power[s]',1.7082760855555534,2.5318157202564180,1.5936009916476905,2.9816418644040823,2.6165633727796376,1.7934732129797339,2.0368359824642539,1.3754424522630870,2.2234877231530845,1.9732759967446327]
samplesNames = ['','Sample1','Sample2','Sample3','Sample4','Sample5',
               'Sample6','Sample7','Sample8','Sample9','Sample10']
inputsProp = pd.DataFrame([samplesNames,velocity,power,powerOnOff])
inputsamples = inputsProp.transpose()

