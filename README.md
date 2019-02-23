# RainfallAlarm
RainfallAlarm is a platform based on Image Processing techniques and Convolutional Neural Networks to track clouds, aiming to predict and quantify the geolocalized rainfalls for the next 2 hours.

meteorological data is scrapped from http://www.meteo.cat/observacions/radar . Overall, this information is extracted every 6 minutes:
  - cloud intensity maps of quadrants of the map

![image](https://user-images.githubusercontent.com/4817932/53279235-fae6a480-370e-11e9-8255-6cb8285fc221.png)

- temperature, humidity, pressure and wind intensity/direction values for each of the 68 Stations in the map 

![image](https://user-images.githubusercontent.com/4817932/53284055-db6f6c00-374e-11e9-8e47-6bbccd2ac62a.png)
