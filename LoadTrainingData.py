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
    
    Stations = ['La seu Urgell', 'El pont de Suert', 'Nuria', 'Mollo' ,'Espolla', 'Portbou', 'Roses', 'Castello Empuries', 'Cabanes' ,'Vall den Bas', 'Queralt', 'Lladurs', 'Oliana', 'Organyà', 'Sant pere pescador', 'Tallada de Empordà', 'La bisbal de Empordà', 'Cassà de la selva', 'Viloví Onyà', 'Viladrau', 'Puig Sessolles', 'Artés', 'El pont de vilomara', 'Sant Llorenç Savall', 'Sant Salvador de Guardiola', 'Rellinars', 'La panadella', 'Cervera', 'El Canós', 'CastellNou de Seana', 'Vallfogona de Balaguer', 'Els Alamús', 'Alguaire', 'Alfarràs', 'Albesa', 'Gimenells', 'Raimat', 'Golmés', 'El Poal', 'Òdena', 'Montserrat', 'Hostalets de Pierola', 'Caldes de Montbui', 'Malgrat de Mar', 'Cabrils', 'Barcelona El Raval', 'El Prat ', 'Vallirana', 'Cunit', 'El Vendrell', 'La Bisbal del penedès', 'Nulles', 'Torredembarra', 'Constantí', 'Espluga del Francolí', 'Torroja del Priorat', 'Torres del Segre', 'Aitona', 'Maials', 'El Masroig', 'Benissanet', 'Gandesa', 'Batea', 'PN dels ports', 'Illa de buda', 'Amposta', 'Mas de Barberans', 'Ulldecona']
    Codes= ['CD', 'CT', 'DG', 'CG', 'VZ', 'D6', 'D4', 'W1', 'U1', 'W9', 'WM', 'VO', 'W5', 'CJ', 'U2', 'UB', 'DF', 'UN', 'VN', 'WS', 'XK', 'WW', 'R1', 'VV', 'CL', 'VU', 'XA', 'C8', 'VD', 'C6', 'V1', 'XM', 'X3', 'WK', 'WB', 'VH', 'VK', 'WC', 'V8', 'H1', 'WN', 'CE', 'X9', 'WT', 'UP', 'X4', 'XL', 'D3', 'WZ', 'D9', 'WO', 'VY', 'DK', 'VQ', 'CW', 'WR', 'X7', 'VE', 'WI', 'WJ', 'VB', 'XP', 'WD', 'X5', 'DL', 'UU', 'C9', 'UX']
    PosX=[388, 322, 448, 476, 529, 540, 546, 538, 528, 473, 420, 391, 373, 377, 535, 534, 532, 518, 505, 471, 479, 433, 427, 422, 417, 430, 386, 370, 364, 343, 328, 321, 307, 306, 316, 297, 307, 341, 331, 401, 421, 417, 453, 503, 467, 454, 444, 429, 399, 395, 387, 376, 383, 366, 353, 330, 302, 296, 300, 323, 314, 294, 281, 300, 322, 307, 286, 292]
    PosY=[343, 336, 339, 342, 337, 335, 354, 353, 347, 373, 371, 383, 379, 360, 364, 376, 592, 402, 403, 405, 417, 410, 425, 427, 427, 432, 436, 427, 417, 429, 419, 434, 419, 409, 419, 428, 432, 432, 426, 433, 433, 445, 434, 430, 444, 462, 470, 466, 483, 481, 472, 474, 490, 489, 461, 481, 442, 449, 464, 493, 505, 502, 497, 525, 545, 542, 542, 555] 
    
    NumStations=len(Codes)
    AvTemp=np.ones(NumStations)
    MaxTemp=np.ones(NumStations)
    MinTemp=np.ones(NumStations)
    Humidity=np.ones(NumStations)

    img = Image.open(BytesIO(requests.get("http://static-m.meteo.cat/tiles/fons/GoogleMapsCompatible/07/000/000/063/000/000/081.png").content))
    img1 = Image.new('L',img.size,0)
    
    i=0
    
    im_array=[]
    AvTempMap=[]
    MaxTempMap=[]
    MinTempMap=[]
    HumidityMap=[]
    
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
                print( '  .  .  .  ' + ' image #' +  str(i) + ' found at %s/%s/%s %s:%s:%s' %(str(year),str(month),str(day),str(hour),str(round_minute),str(second)) + ' - ' + str(time_slot) )
                img_i=merge3x3(im_parts_array)
                im_array.append(img_i)
                imgfound=True
                
                for x in range (0, len(Codes)): 
                    page=requests.get('http://www.meteo.cat/observacions/xema/dades?codi=' + str(Codes[x])+'&dia='+str(year[0])+'-'+str(month[0])+'-'+str(day[0])+'T'+str(hour[0])+':00Z')
                    soup = BS(page.text, 'html.parser')
                    AvTemp[x]=extract_nbr(str(soup.select("table tbody tr td")[0]))
                    MaxTemp[x]=extract_nbr(str(soup.select("table tbody tr td")[1]))
                    MinTemp[x]=extract_nbr(str(soup.select("table tbody tr td")[3]))
                    Humidity[x]=extract_nbr(str(soup.select("table tbody tr td")[5]))
                    
                    AvTempMap.append(expand_Values_in_Map( PosX, PosY, AvTemp,   'avgTempMap.png'))
                    MaxTempMap.append(expand_Values_in_Map( PosX, PosY, MaxTemp,  'maxTempMap.png'))
                    MinTempMap.append(expand_Values_in_Map( PosX, PosY, MinTemp,  'minTempMap.png'))
                    HumidityMap.append(expand_Values_in_Map( PosX, PosY, Humidity, 'HumidityMap.png'))
                    
                print( '  .  .  .  ' + ' avg, min and max Temp maps of frame #' +  str(i) + ' created at %s/%s/%s %s:%s:%s' %(str(year),str(month),str(day),str(hour),
                
                i=i+1
            if imgfound==True:
                break 
        time.sleep(60*2)
        print ('looping')
    return im_array;
