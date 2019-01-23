## update when geolocalization code is written. 

def getLocation():
    ## write code for real geolocalization of user
    pix_X=222
    pix_Y=566
    ## write code for real geolocalization of user
    loc=[pix_X,pix_Y]
    return loc
    
loc=getLocation()
pix_X=loc[0]
pix_Y=loc[1]

rainVal= [None] * len(im_array)
for i in range(0,len(im_array)):
    img_i=arr_equalized[i]
    val=img_i.getpixel((pix_X,pix_Y))
    rainVal[i]=val    
    
rainVal.reverse()
print(rainVal)
plt.xticks(x_n, xaxis,rotation='vertical')
plt.plot(x_n,rainVal)
plt.ylabel('rain intensity')
plt.axis([0, len(im_array), 0, 20])
plt.fill_between(x_n, rainVal, 0)
plt.show()
