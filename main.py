import importlib

import externals
import LoadTrainingData

#__import__ externals.py
#__import__ LoadRealTimeData.py
#__import__ LoadTrainingData.py
#__import__ UNet_3Dto2D.py
#__import__ geo_plot_rainfall.py


LoadTrainingData.load_N_images(1000)
print(N + ' consecutive images loaded - ready to prepare data for training')

# define and call function to prepare data for sets of 10+1 images to be trained.

# train network 

# predict future frames. 

# cast geolocation of user and plot histogram of rainfall. 
