import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageCms
import os

inputFolder = "D:/python-workplace/badge-app/poze"
outputFolder = "D:/python-workplace/badge-app/results"
nr = 2
Colt1 = [0,0]
Colt2 = [300,500]
WidthMin = [0,0,0]
WidthMin[0] = 200
WidthMin[1] = 300
WidthMin[2] = 100
WidthMax = [0,0,0]
WidthMax[0] = 827
WidthMax[1] = 827
WidthMax[2] = 827
Height = [0,0,0]
Height[0] = 720
Height[1] = 850
Height[2] = 0
FontSize = [0,0,0]
FontSize[0] = 90
FontSize[1] = 70
FontSize[2] = 50
FontName = [0,0,0]
FontName[0] = "BebasNeue-Regular"
FontName[1] = "BebasNeue-Regular"
FontName[2] = "BebasNeue-Regular"
TextColor = [0,0,0]
TextColor[0] = eval("(50,50,40,50)")
TextColor[1] = "#ffffff"
TextColor[2] = "#ffffff"
TextAlign = [0,0,0]
TextAlign[0] = "center"
TextAlign[1] = "left"
TextAlign[2] = "right"

def brain(inputFolder, outputFolder, nr, Colt1, Colt2, WidthMin, WidthMax, Height, FontSize, FontName, TextColor, TextAlign ):
    #formatare nume fisierelor in filename list

    filename =[]
    for file in os.listdir(inputFolder):
        x= file.split("_")
        y=x[nr].split(".")
        x[nr]=y[0]
        filename.append(x)

    #init fonturi, Mic e pentru scris pe 2 randuri
    font = [0,0,0,0,0,0]
    fontMic = [0,0,0,0,0,0]
    for i in range(nr):
        font[i] = ImageFont.truetype(FontName[i], int(FontSize[i]* 9/7) )
        fontMic[i] = ImageFont.truetype(FontName[i],int( FontSize[i]*18/21) )

    for x in filename:

        print(x[0])
        cropInfo = x[nr]

        name = x[0]
        for i in range(1,nr+1):
            name = name + "_" + x[i]
        # importare imagine cu badge
        badge = Image.open("badge.jpg", mode='r')
        icc_profile = badge.info.get("icc_profile")
        W,H =badge.size
        imgPers = Image.open(inputFolder + '/' +name+ ".jpg")
        w,h = imgPers.size
        #Taiere pozei ca sa se potriveasca in badge
        canvasWidth = Colt2[0] - Colt1[0]
        canvasHeight = Colt2[1] - Colt1[1]

        if h/w > canvasHeight/canvasWidth:
            rap =canvasWidth/w
            imgPers = imgPers.resize((canvasWidth,int(h*rap) ))
            w,h = imgPers.size
            if cropInfo=='1':
                imgPers = imgPers.crop((0,0,canvasWidth,canvasHeight))
            elif cropInfo=='2':
                imgPers = imgPers.crop( ( 0,h/2-int(canvasHeight/2)  , canvasWidth, h/2+int(canvasHeight/2) )  )
            else:
                imgPers = imgPers.crop((0,h-canvasHeight,canvasWidth,h))
        else:
            rap =canvasHeight/h
            imgPers = imgPers.resize((int(w*rap),canvasHeight ))
            w,h = imgPers.size
            if cropInfo=='1':
                imgPers = imgPers.crop((0,0,canvasWidth,canvasHeight))
            elif cropInfo=='2':
                imgPers = imgPers.crop((w/2-int(canvasWidth/2),0,w/2+int(canvasWidth/2),canvasHeight))
            else:
                imgPers = imgPers.crop((w-canvasWidth,0,w,canvasHeight))

        badge.paste(imgPers, (Colt1[0],Colt1[1]) )
        draw = ImageDraw.Draw(badge)

        for i in range(nr):
            wnume, hnume = draw.textsize(x[i] , font=font[i])
            if TextAlign[i] == 'center':
            #cazuri pentru scris numele pe mai multe linii
                if (wnume< WidthMax[i] - WidthMin[i] ):
                    draw.text( (WidthMin[i] + (WidthMax[i] - WidthMin[i] - wnume)/2,Height[i])   ,x[i],fill = TextColor[i], font=font[i] )
                else:
                    numeList = x[i].split(" ")
                    if(len(numeList)==2):
                        wnume,hnume = draw.textsize(numeList[0], font=fontMic[i])
                        draw.text( (WidthMin[i] + (WidthMax[i] - WidthMin[i] - wnume)/2,Height[i]) ,numeList[0], fill = TextColor[i], font=fontMic[i] )
                        wnume,hnume = draw.textsize(numeList[1], font=fontMic[i])
                        draw.text( (WidthMin[i] + (WidthMax[i] - WidthMin[i] - wnume)/2,Height[i] + int( FontSize[i]*2/3) ) ,numeList[1],fill = TextColor[i], font=fontMic[i] )
                    elif(len(numeList)>2):
                        cuv=1
                        linia1 = numeList[0]
                        wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                        wnumeUrm, hnumeUrm = draw.textsize(numeList[1], font=fontMic[i])
                        while wnume+wnumeUrm < WidthMax[i] - WidthMin[i] and cuv <len(numeList)-1:
                            linia1 = linia1 +" "+ numeList[cuv]
                            wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                            cuv+=1
                            wnumeUrm, hnumeUrm = draw.textsize(numeList[cuv], font=fontMic[i])

                        linia2 = ''
                        for k in range(cuv,len(numeList)):
                            linia2 = linia2+ numeList[k]+' '


                        linia2=linia2[:-1]
                        wnume,hnume = draw.textsize(linia1, font=fontMic[i])

                        draw.text ( (WidthMin[i] + (WidthMax[i] - WidthMin[i] - wnume)/2,Height[i] ),linia1, fill =TextColor[i], font=fontMic[i] )
                        wnume,hnume = draw.textsize(linia2, font=fontMic[i])
                        draw.text ( (WidthMin[i] + (WidthMax[i] - WidthMin[i] - wnume)/2,Height[i]+ int( FontSize[i]*2/3) ),linia2, fill = TextColor[i], font=fontMic[i] )

            elif TextAlign[i] == "left":
                if (wnume< WidthMax[i] - WidthMin[i] ):
                    draw.text( (WidthMin[i] , Height[i])   ,x[i], fill = TextColor[i], font=font[i] )
                else:
                    numeList = x[i].split(" ")
                    cuv=1
                    linia1 = numeList[0]
                    wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                    wnumeUrm, hnumeUrm = draw.textsize(numeList[1], font=fontMic[i])
                    while wnume+wnumeUrm < WidthMax[i] - WidthMin[i] and cuv <len(numeList)-1:
                        linia1 = linia1 +" "+ numeList[cuv]
                        wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                        cuv+=1
                        if cuv<len(numeList):
                            wnumeUrm, hnumeUrm = draw.textsize(numeList[cuv], font=fontMic[i])
                        else:
                            break
                    linia2 = ''
                    for k in range(cuv,len(numeList)):
                        linia2 = linia2+ numeList[k]+' '
                    linia2=linia2[:-1]
                    wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                    draw.text ( (WidthMin[i] , Height[i] ),linia1, fill =TextColor[i], font=fontMic[i] )
                    wnume,hnume = draw.textsize(linia2, font=fontMic[i])
                    draw.text ( (WidthMin[i] , Height[i]+ int( FontSize[i]*2/3)+10 ),linia2, fill = TextColor[i], font=fontMic[i] )

            else:
                if (wnume< WidthMax[i] - WidthMin[i] ):
                    draw.text( (WidthMax[i]-wnume , Height[i])   ,x[i], fill = TextColor[i], font=font[i] )
                else:
                    numeList = x[i].split(" ")
                    cuv=1
                    linia1 = numeList[0]
                    wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                    wnumeUrm, hnumeUrm = draw.textsize(numeList[1], font=fontMic[i])
                    while wnume+wnumeUrm < WidthMax[i] - WidthMin[i] and cuv <len(numeList)-1:
                        linia1 = linia1 +" "+ numeList[cuv]
                        wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                        cuv+=1
                        if cuv<len(numeList):
                            wnumeUrm, hnumeUrm = draw.textsize(numeList[cuv], font=fontMic[i])
                        else:
                            break
                    linia2 = ''
                    for k in range(cuv,len(numeList)):
                        linia2 = linia2+ numeList[k]+' '
                    linia2=linia2[:-1]
                    wnume,hnume = draw.textsize(linia1, font=fontMic[i])
                    wnume2,hnume2 = draw.textsize(linia2, font=fontMic[i])

                    draw.text ( (WidthMax[i]-wnume , Height[i] ),linia1, fill =TextColor[i], font=fontMic[i] )
                    wnume,hnume = draw.textsize(linia2, font=fontMic[i])
                    draw.text ( (WidthMax[i]-wnume2 , Height[i]+ int( FontSize[i]*2/3)+10 ),linia2, fill = TextColor[i], font=fontMic[i] )



        badge.paste(imgPers, (Colt1[0],Colt1[1]) )

        badge.save(outputFolder+"/"+x[0]+'.jpg', quality = 100, icc_profile=icc_profile)

    print('Done')
