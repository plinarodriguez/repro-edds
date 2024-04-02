# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# Set the font family and size to use for Matplotlib figures.
plt.rcParams['font.size'] = 17
# Geometry
labels = ['Mouthpiece','Pipe','Atomizer','Inlet Pipe']
diam = [8.02,4.54,4.54,4.54]
length = [13.96,27.955,7.5,2.17]
thick = [0.13,0.15,0.15,0.15]
geom_db = pd.DataFrame({'label':labels,'Diameter[mm]':diam,'Length[mm]':length,'Thickness[mm]':thick})
coil10 = {'Coil_qty':10,'Coil_Diameter':0.3,'Coil_Spacing':0.5} #label,qty,outter diameter,single coil diameter,space btw coils
# Mesh Details
mesh_stats = {'Nodes':2278204,'Elements':13225239}

