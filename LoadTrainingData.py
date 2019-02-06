import datetime
import numpy as np
import urllib
import time

import io
import os
from matplotlib import pyplot as plt
from datetime import timedelta
import sys
from PIL import Image
import requests
from io import BytesIO

import requests
import math
from bs4 import BeautifulSoup as BS
import numpy as np

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def merge3x3(arrImg):
    imgtop = Image.new("RGB", (768,256))
    arrImg[0].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[0].size
    imgtop.paste(arrImg[0], (0, 0, w, h))
    arrImg[1].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[1].size
    imgtop.paste(arrImg[1], (256,0 , w+256, h))
    arrImg[2].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[2].size
    imgtop.paste(arrImg[2], (512,0, w+512, h))
    
    imgmiddle = Image.new("RGB", (768,256))
    arrImg[3].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[3].size
    imgmiddle.paste(arrImg[3], (0, 0, w, h))
    arrImg[4].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[4].size
    imgmiddle.paste(arrImg[4], (256,0 , w+256, h))
    arrImg[5].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[5].size
    imgmiddle.paste(arrImg[5], (512,0, w+512, h))
    
    imgbottom = Image.new("RGB", (768,256))
    arrImg[6].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[6].size
    imgbottom.paste(arrImg[6], (0, 0, w, h))
    arrImg[7].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[7].size
    imgbottom.paste(arrImg[7], (256,0 , w+256, h))
    arrImg[8].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[8].size
    imgbottom.paste(arrImg[8], (512,0, w+512, h))
    
    imgtot = Image.new("RGB", (768,768))
    imgtop.thumbnail((768, 256), Image.ANTIALIAS)
    w, h = imgtop.size
    imgtot.paste(imgtop, (0, 0, w, h))
    imgmiddle.thumbnail((768, 256), Image.ANTIALIAS)
    w, h = imgmiddle.size
    imgtot.paste(imgmiddle, (0,256 , w, h+256))
    imgbottom.thumbnail((768, 512), Image.ANTIALIAS)
    w, h = imgbottom.size
    imgtot.paste(imgbottom, (0,512 , w, h+512))
    return imgtot

def ImagetoArr(Img):
    im = Img.convert('L')
    arr = np.fromiter(iter(im.getdata()), np.uint8)
    arr.resize(im.height, im.width)
    return arr

def load_map():
    im_array=[]
    img1 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/063/000/000/081.png").content))
    im_array.append( img1 )
    img2 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/064/000/000/081.png").content))
    im_array.append( img2 )
    img3 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/065/000/000/081.png").content))
    im_array.append( img3 )
    img4 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/063/000/000/080.png").content))
    im_array.append( img4 )
    img5 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/064/000/000/080.png").content))
    im_array.append( img5 )
    img6 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/065/000/000/080.png").content))
    im_array.append( img6 )
    img7 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/063/000/000/079.png").content))
    im_array.append( img7 )
    img8 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/064/000/000/079.png").content))
    im_array.append( img8 )
    img9 = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/065/000/000/079.png").content))
    im_array.append( img9 )
    mapa=merge3x3(im_array)
    return mapa

def load_N_images(N):
    img = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/063/000/000/081.png").content))
    img1 = Image.new('L',img.size,0)
    i=0
    im_array=[]
    sizeImg = img1.size
    mapa=load_map
    minute=0
    lasturl='http://static-m.meteo.cat/tiles/radar/2018/03/09/15/42/07/000/000/063/000/000/080.png'
    print ('strating the collection of ' + str(N) + ' consecutive images')
    while i<N:
    
        time_slot=str(datetime.datetime.now() - timedelta(hours = 2))
        year=(time_slot[0:4])
        month=(time_slot[5:7])
        day=(time_slot[8:10])
        h=int(float(time_slot[11:13]))
        hour=(str(h) )
        minute=time_slot[14:16]
        im_parts_array=[]
        if int(minute)<6:
            round_minute=('00')
        elif int(minute)<12:
            round_minute=('06')
        elif int(minute)<18:
            round_minute=('12')
        elif int(minute)<24:
            round_minute=('18')
        elif int(minute)<30:
            round_minute=('24')
        elif int(minute)<36:
            round_minute=('30')
        elif int(minute)<42:
            round_minute=('36')
        elif int(minute)<48:
            round_minute=('42')
        elif int(minute)<54:
            round_minute=('48')
        elif int(minute)<60:
            round_minute=('54')
        j=0
        imgfound=False
        for j in range(0,60):             
            sec=str(j).zfill(2)   
            url=('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/079.png' % (str(year),str(month),str(day),str(hour),str(round_minute),str(sec)))
            if exists(url) and (url != lasturl):
                                                                                                          
                lasturl=url
                second=('%02i'%j)
                try:
                    img1 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/063/000/000/081.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))
                except:
                    img1 = Image.new('L',sizeImg,0)
                im_parts_array.append( img1 )
                try:
                    img2 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/081.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))
                except:
                    img2 = Image.new('L',sizeImg,0)
                im_parts_array.append( img2 )
                try:
                    img3 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/065/000/000/081.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))   
                except:
                    img3 = Image.new('L',sizeImg,0)
                im_parts_array.append( img3 )
                try:
                    img4 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/063/000/000/080.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content)) 
                except:
                    img4 = Image.new('L',sizeImg,0)
                im_parts_array.append( img4 )
                try:
                    img5 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/080.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))  
                except:
                    img5 = Image.new('L',sizeImg,0)
                im_parts_array.append( img5 )
                try:
                    img6 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/065/000/000/080.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))  
                except:
                    img6 = Image.new('L',sizeImg,0)
                im_parts_array.append( img6 )
                try:
                    img7 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/063/000/000/079.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))  
                except:
                    img7 = Image.new('L',sizeImg,0)
                im_parts_array.append( img7 )
                try:
                    img8 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/079.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))  
                except:
                    img8 = Image.new('L',sizeImg,0)
                im_parts_array.append( img8 )
                try:
                    img9 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/065/000/000/079.png'%(str(year),str(month),str(day),str(hour),str(round_minute),str(second))).content))  
                except:
                    img9 = Image.new('L',sizeImg,0)
                im_parts_array.append( img9 )
                print( '  .  .  .  ' + ' image #' +  str(i) + ' found at %s/%s/%s %s:%s:%s' %(str(year),str(month),str(day),str(hour),str(round_minute),str(second)) + ' - ' + str(time_slot) + ' - ' + str(datetime.datetime.now()))
                img_i=merge3x3(im_parts_array)
                im_array.append(img_i)
                imgfound=True
                time.sleep(60*4)
                i=i+1
            if imgfound==True:
                break 
        time.sleep(60*2)
        print ('looping')
    return im_array;
