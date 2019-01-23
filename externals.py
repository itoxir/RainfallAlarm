import datetime
import numpy as np
import urllib
import io
from matplotlib import pyplot as plt
from datetime import timedelta
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from PIL import Image
import requests
import math
import cv2
from bs4 import BeautifulSoup as BS
pathDropbox='C:/Users/itoxi/Dropbox/RAinDar'

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(h):
    return(tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))

def merge3x3(arrImg):
    imgtop = Image.new("RGB", (768,256))
    arrImg[0].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[0].size
    imgtop.paste(arrImg[0], (0, 0, w, h))
    arrImg[1].thumbnail((256, 256), Image.ANTIALIAS)
    w, h = arrImg[1].sizemeteo
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

def ImagetoArr(Img):
    im = Img.convert('L')
    arr = np.fromiter(iter(im.getdata()), np.uint8)
    arr.resize(im.height, im.width)
    return arr

def color_separator(im):
    if im.getpalette():
        im = im.convert('RGB')

    colors = im.getcolors()
    width, height = im.size
    colors_dict = dict((val[1],Image.new('RGB', (width, height), (0,0,0))) 
                        for val in colors)
    pix = im.load()    
    for i in range(width):
        for j in range(height):
            colors_dict[pix[i,j]].putpixel((i,j), pix[i,j])
    return colors_dict

def equalizeImg(colors_dict,RGBS):
    temp=list(color_dict.values())
    img_out = np.zeros((temp[0].size), np.uint8)
    key=list(color_dict.keys())
    for i in range(0,len(colors_dict.keys())):
        for j in range(0,len(RGBS)):
            if (key[i]==RGBS[j]):
                image_file = temp[i].convert('L') # convert image to black and white 
                image_cv=ImagetoArr(image_file)
                val, img_bin=cv2.threshold(image_cv,1,255,cv2.THRESH_OTSU)
                #print('weight '+ str(j+1))
                img_bin=img_bin/255
                img_bin=img_bin*(j+1)
                #print('max ' + str(img_bin.max()))
                img_out=img_out+img_bin 
    #print('max ' + str(img_out.max()))    
    #img_out=img_out*124
    img = Image.fromarray(img_out, 'L')
    return img

def extract_nbr(input_str):
    if input_str is None or input_str == '':
        return 0
    deci=False
    out_number = ''
    startcounting=False
    for ele in input_str:
        if ele=='>':
            startcounting=True
        if startcounting==True:
            if ele.isdigit() and deci==False:
                out_number += ele
            elif ele=='.':
                out_number=float(out_number) 
                deci=True
            if ele.isdigit() and deci==True: 
                out_number += float(ele)*0.1

    return float(out_number)   
    
    from PIL import Image
import requests
from io import BytesIO

img = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/063/000/000/081.png").content))
img1 = Image.new('L',img.size,0)


def expand_Values_in_Map(PposX,PposY,Pvals):
    im = Image.open('mapa.png')
    out = im.convert("L")
    px = out.load()
    for i in range(0,out.size[1]):
        for y in range(0,out.size[1]):
            px[i,y]=0
    numPoints=len(Pvals)
    acumX=0
    acumY=0
    for l in range(0,700):
        X=-math.pow(-1,l)
        Y=-math.pow(-1,l)
        for k in range(1,l):
            for p in range(0,numPoints):
                try:
                    if px[PposX[numPoints-p]+acumX,PposY[numPoints-p]+acumY]==0:
                        px[PposX[numPoints-p]+acumX,PposY[numPoints-p]+acumY]=int(Pvals[numPoints-p])
                except:
                    '''do nothing'''
            acumX=acumX+X
        for k in range(1,l):
            for p in range(0,numPoints):
                try:
                    if px[PposX[numPoints-p]+acumX,PposY[numPoints-p]+acumY]==0:
                        px[PposX[numPoints-p]+acumX,PposY[numPoints-p]+acumY]=int(Pvals[numPoints-p])
                except:
                    '''do nothing'''
            acumY=acumY+Y  
    outarray=np.asarray(out)
    out.save('example2.png')
    return outarray

hex_01="8000FF"
rgb1=hex2rgb(hex_01)
hex_02="4000FF"
rgb2=hex2rgb(hex_02)
hex_03="0000FF"
rgb3=hex2rgb(hex_03)
hex_04="00FFFF"
rgb4=hex2rgb(hex_04)
hex_05="00FF80"
rgb5=hex2rgb(hex_05)
hex_06="00FF00"
rgb6=hex2rgb(hex_06)
hex_07="3FFF00"
rgb7=hex2rgb(hex_07)
hex_08="7FFF00"
rgb8=hex2rgb(hex_08)
hex_09="BFFF00"
rgb9=hex2rgb(hex_09)
hex_10="FFFF00"
rgb10=hex2rgb(hex_10)
hex_11="FFAB00"
rgb11=hex2rgb(hex_11)
hex_12="FF8100"
rgb12=hex2rgb(hex_12)
hex_13="FF5700"
rgb13=hex2rgb(hex_13)
hex_14="FF2D00"
rgb14=hex2rgb(hex_14)
hex_15="FF0000"
rgb15=hex2rgb(hex_15)
hex_16="FF003F"
rgb16=hex2rgb(hex_16)
hex_17="FF007F"
rgb17=hex2rgb(hex_17)
hex_18="FF00BF"
rgb18=hex2rgb(hex_18)
hex_19="FF00FF"
rgb19=hex2rgb(hex_19)
hex_20="FFFFFF"
rgb20=hex2rgb(hex_20)

RGBS=[rgb1,rgb2,rgb3,rgb4,rgb5,rgb6,rgb7,rgb8,rgb9,rgb10,rgb11,rgb12,rgb13,rgb14,rgb15,rgb16,rgb17,rgb18,rgb19,rgb20]

print ('definitions and imports loaded - colors labels loaded - map loaded')
