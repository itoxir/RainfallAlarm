
initial_delay = 2
acumdelay=0
num_prev_images=12
delays=[num_prev_images]
year=[]
month=[]
day=[]
hour=[]
minute=0
round_minute=[]
name_img_url=[]
im_array=[]
second=[]
sizeImg = img1.size
mapa=load_map
num_foundImgs=0
xaxis= [None] * num_prev_images
x_n= [None] * num_prev_images
print (' > finding images . . . <')
    
for x in range(0,num_prev_images):
    delays.append(acumdelay)
    delays.append(acumdelay)
    time_slot=str(datetime.datetime.now() - timedelta(hours = 2) - timedelta(minutes = initial_delay) - timedelta(minutes = acumdelay))
    year.append(time_slot[0:4])
    month.append(time_slot[5:7])
    day.append(time_slot[8:10])
    h=int(float(time_slot[11:13]))
    hour.append(str(h).zfill(2) )
    minute=time_slot[14:16]
    im_parts_array=[]
    if int(minute)<6:
        round_minute.append('00')
    elif int(minute)<12:
        round_minute.append('06')
    elif int(minute)<18:
        round_minute.append('12')
    elif int(minute)<24:
        round_minute.append('18')
    elif int(minute)<30:
        round_minute.append('24')
    elif int(minute)<36:
        round_minute.append('30')
    elif int(minute)<42:
        round_minute.append('36')
    elif int(minute)<48:
        round_minute.append('42')
    elif int(minute)<54:
        round_minute.append('48')
    elif int(minute)<60:
        round_minute.append('54')
    j=0
    xaxis[x]=str(hour[x])+':'+str(round_minute[x])
    imgfound=False

    for j in range(0,60):             
        sec=str(j).zfill(2)   
        url=('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/079.png' % (str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(sec)))
        #print(url)http://static-m.meteo.cat/tiles/radar/2018/03/09/15/42/07/000/000/063/000/000/080.png
        if exists(url):
            x_n[x]=x
            second.append('%02i'%j)
            try:
                img1 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/063/000/000/081.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))
            except:
                img1 = Image.new('L',sizeImg,0)
            im_parts_array.append( img1 )
            try:
                img2 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/081.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))
            except:
                img2 = Image.new('L',sizeImg,0)
            im_parts_array.append( img2 )
            try:
                img3 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/065/000/000/081.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))   
            except:
                img3 = Image.new('L',sizeImg,0)
            im_parts_array.append( img3 )
            try:
                img4 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/063/000/000/080.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content)) 
            except:
                img4 = Image.new('L',sizeImg,0)
            im_parts_array.append( img4 )
            try:
                img5 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/080.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))  
            except:
                img5 = Image.new('L',sizeImg,0)
            im_parts_array.append( img5 )
            try:
                img6 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/065/000/000/080.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))  
            except:
                img6 = Image.new('L',sizeImg,0)
            im_parts_array.append( img6 )
            try:
                img7 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/063/000/000/079.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))  
            except:
                img7 = Image.new('L',sizeImg,0)
            im_parts_array.append( img7 )
            try:
                img8 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/064/000/000/079.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))  
            except:
                img8 = Image.new('L',sizeImg,0)
            im_parts_array.append( img8 )
            try:
                img9 = Image.open(BytesIO(requests.get('http://static-m.meteo.cat/tiles/radar/%s/%s/%s/%s/%s/%s/000/000/065/000/000/079.png'%(str(year[x]),str(month[x]),str(day[x]),str(hour[x]),str(round_minute[x]),str(second[x]))).content))  
            except:
                img9 = Image.new('L',sizeImg,0)
            im_parts_array.append( img9 )
            print( '  .  .  .  ' + ' image #' +  str(x) + ' found at %s/%s/%s %s:%s:%s' %(str(year[x]),str(month[x]),str(day[x]),str(int(float(hour[x]))+2),str(round_minute[x]),str(second[x])))
            img_i=merge3x3(im_parts_array)
            im_array.append(img_i)
            imgfound=True
            acumdelay=acumdelay+6
            num_foundImgs=num_foundImgs+1
        if imgfound==True:
            break 
            
xaxis.reverse()
for i in range(0,len(im_array)):
    imi=im_array[i]
    imi.save( pathDropbox + '/temp/img' +str(i)+'.png')
    #print '  .  .  .  image ' + str(i) + '/' + str(len(im_array)-1) + ' saved in /Users/itoxir/Documents/Projectes/plujesNow/temp/'

if num_prev_images==num_foundImgs:
    print (' > all images found and stored <')

print (' > finding correspondence with cloud intensity . . . <')
arr_equalized=[]
imgout=[]
for i in range(0,len(im_array)):
    color_dict=color_separator(im_array[i])
    img=equalizeImg(color_dict,RGBS, i)
    arr_equalized.append(img)
    #imin,imax=img.getextrema()
    #nameis='img'+str(i)
    #print(nameis)
    img = Image.fromarray(np.uint8(img*12.75) , 'L')
    img.save(pathDropbox + '/temp/'+str(i)+'.png')
    imgout.append(np.asarray(img))
imgout=np.asarray(imgout)

print ('  .  .  .  done ')

Stations = ['La seu Urgell', 'El pont de Suert', 'Nuria', 'Mollo' ,'Espolla', 'Portbou', 'Roses', 'Castello Empuries', 'Cabanes' ,'Vall den Bas', 'Queralt', 'Lladurs', 'Oliana', 'Organyà', 'Sant pere pescador', 'Tallada de Empordà', 'La bisbal de Empordà', 'Cassà de la selva', 'Viloví Onyà', 'Viladrau', 'Puig Sessolles', 'Artés', 'El pont de vilomara', 'Sant Llorenç Savall', 'Sant Salvador de Guardiola', 'Rellinars', 'La panadella', 'Cervera', 'El Canós', 'CastellNou de Seana', 'Vallfogona de Balaguer', 'Els Alamús', 'Alguaire', 'Alfarràs', 'Albesa', 'Gimenells', 'Raimat', 'Golmés', 'El Poal', 'Òdena', 'Montserrat', 'Hostalets de Pierola', 'Caldes de Montbui', 'Malgrat de Mar', 'Cabrils', 'Barcelona El Raval', 'El Prat ', 'Vallirana', 'Cunit', 'El Vendrell', 'La Bisbal del penedès', 'Nulles', 'Torredembarra', 'Constantí', 'Espluga del Francolí', 'Torroja del Priorat', 'Torres del Segre', 'Aitona', 'Maials', 'El Masroig', 'Benissanet', 'Gandesa', 'Batea', 'PN dels ports', 'Illa de buda', 'Amposta', 'Mas de Barberans', 'Ulldecona']
Codes= ['CD', 'CT', 'DG', 'CG', 'VZ', 'D6', 'D4', 'W1', 'U1', 'W9', 'WM', 'VO', 'W5', 'CJ', 'U2', 'UB', 'DF', 'UN', 'VN', 'WS', 'XK', 'WW', 'R1', 'VV', 'CL', 'VU', 'XA', 'C8', 'VD', 'C6', 'V1', 'XM', 'X3', 'WK', 'WB', 'VH', 'VK', 'WC', 'V8', 'H1', 'WN', 'CE', 'X9', 'WT', 'UP', 'X4', 'XL', 'D3', 'WZ', 'D9', 'WO', 'VY', 'DK', 'VQ', 'CW', 'WR', 'X7', 'VE', 'WI', 'WJ', 'VB', 'XP', 'WD', 'X5', 'DL', 'UU', 'C9', 'UX']
PosX=[388, 322, 448, 476, 529, 540, 546, 538, 528, 473, 420, 391, 373, 377, 535, 534, 532, 518, 505, 471, 479, 433, 427, 422, 417, 430, 386, 370, 364, 343, 328, 321, 307, 306, 316, 297, 307, 341, 331, 401, 421, 417, 453, 503, 467, 454, 444, 429, 399, 395, 387, 376, 383, 366, 353, 330, 302, 296, 300, 323, 314, 294, 281, 300, 322, 307, 286, 292]
PosY=[343, 336, 339, 342, 337, 335, 354, 353, 347, 373, 371, 383, 379, 360, 364, 376, 592, 402, 403, 405, 417, 410, 425, 427, 427, 432, 436, 427, 417, 429, 419, 434, 419, 409, 419, 428, 432, 432, 426, 433, 433, 445, 434, 430, 444, 462, 470, 466, 483, 481, 472, 474, 490, 489, 461, 481, 442, 449, 464, 493, 505, 502, 497, 525, 545, 542, 542, 555] 

NumStations=len(Codes)
AvTemp=np.ones(NumStations)
MaxTemp=np.ones(NumStations)
MinTemp=np.ones(NumStations)
Humidity=np.ones(NumStations)
print (' > calculating temperature and humidity maps')
print ('  .  .  .  location - av. temp - max t - min t - humidity')

for x in range (0, len(Codes)): 
    page=requests.get('http://www.meteo.cat/observacions/xema/dades?codi=' + str(Codes[x])+'&dia='+str(year[0])+'-'+str(month[0])+'-'+str(day[0])+'T'+str(hour[0])+':00Z')
    soup = BS(page.text, 'html.parser')
    AvTemp[x]=extract_nbr(str(soup.select("table tbody tr td")[0]))
    MaxTemp[x]=extract_nbr(str(soup.select("table tbody tr td")[1]))
    MinTemp[x]=extract_nbr(str(soup.select("table tbody tr td")[3]))
    Humidity[x]=extract_nbr(str(soup.select("table tbody tr td")[5]))
    print (str( '  .  .  .  ' + Stations[x]) + ' has: ' + str(AvTemp[x]) + ' - ' + str(MaxTemp[x]) + ' - ' + str(MinTemp[x]) + ' - ' + str(Humidity[x]))

AvTempMap   = expand_Values_in_Map( PosX, PosY, AvTemp,   'avgTempMap.png')
MaxTempMap  = expand_Values_in_Map( PosX, PosY, MaxTemp,  'maxTempMap.png')
MinTempMap  = expand_Values_in_Map( PosX, PosY, MinTemp,  'minTempMap.png')
HumidityMap = expand_Values_in_Map( PosX, PosY, Humidity, 'HumidityMap.png')

print (' > avTemp, minTemp, maxTemp and Humidity maps calculated and stored')
