import importlib
import datetime
import numpy as np
import urllib
import io
from matplotlib import pyplot as plt
from datetime import timedelta
import sys
#sys.path.append('/usr/local/lib/python2.7/site-packages')
from PIL import Image
import requests
import math
from bs4 import BeautifulSoup as BS
from PIL import Image
import requests
from io import BytesIO

pathDropbox='C:/Users/itoxi/Dropbox/RAinDar

import externals
import LoadTrainingData

#__import__ externals.py
#__import__ LoadRealTimeData.py
#__import__ LoadTrainingData.py
#__import__ UNet_3Dto2D.py
#__import__ geo_plot_rainfall.py

RGBS = externals.load_colors()

externals.load_map()

imgs = LoadTrainingData.load_N_images(1000)

print(N + ' consecutive images loaded - ready to prepare data for training')

# define and call function to prepare data for sets of 10+1 images to be trained.

# train network 

# predict future frames. 

# cast geolocation of user and plot histogram of rainfall. 
