def load_N_images(N):
    
    i=0
    im_array=[]
    sizeImg = img1.size
    mapa=load_map
    minute=0
    lasturl='http://static-m.meteo.cat/tiles/radar/2018/03/09/15/42/07/000/000/063/000/000/080.png'
    print ('strating the collection of ' + N + ' consecutive images')
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
                print( '  .  .  .  ' + ' image #' +  str(i) + ' found at %s/%s/%s %s:%s:%s' %(str(year),str(month),str(day),hour,str(round_minute),str(second)) + ' - ' + str(datetime.datetime.now()))
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
