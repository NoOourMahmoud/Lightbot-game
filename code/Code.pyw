#Bordes -
#357-484:548-615
import pygame,random,sys,os,copy,time
#Form Dimentionals
formWidth=1200#800
formHeight=765#600
formMidWidth=int(formWidth/2)
formMidHeight=int(formHeight/2)
#Colors
white=(255,255,255)
maroon=(128,0,0)
navy=(0,0,128)
lightslategray=(119,136,153)
silver=(192,192,192)

levels=open("levels - Copy.txt","r")
x=levels.readlines()
y=[]
z=[]
for line in x:
    if(not line.startswith('\r') ):    
        y.append(line.rstrip())
    else:
        z.append(y)
        y=[]
gameLevels=z

def main():
    global screenSurface,FPS,basicFont,imageDic,playerPosition,currentLevel,robotBosition,mousePosition,mouseClick,helpImageDic
    pygame.init()
    
    screenSurface=pygame.display.set_mode((formWidth,formHeight), pygame.FULLSCREEN)
    pygame.display.set_caption("GAME")    
    basicFont=pygame.font.SysFont("twcen",28)
    clock=pygame.time.Clock()
    #pygame.mixer.music.load('ip.mp3')
    pygame.mixer.music.load('ip2.mp3')
    
    imageDic = {'1': pygame.image.load('1.png'),
                '2': pygame.image.load('2.png'),
                '3': pygame.image.load('3.png'),
                '4': pygame.image.load('4.png'),
                '5': pygame.image.load('5.png'),

                'a': pygame.image.load('6.png'),
                'b': pygame.image.load('7.png'),
                'c': pygame.image.load('8.png'),
                'd': pygame.image.load('9.png'),
                'e': pygame.image.load('10.png'),

                'v': pygame.image.load('11.png'),
                'w': pygame.image.load('12.png'),
                'x': pygame.image.load('13.png'),
                'y': pygame.image.load('14.png'),
                'z': pygame.image.load('15.png'),

                'l': pygame.image.load('16.png'),

                ' ': pygame.image.load('space.png'),
                '-': pygame.image.load('space.png'),
                

                'start': pygame.image.load('startButton.png'),

                'mute': pygame.image.load('off.png'),
                'unMute': pygame.image.load('on.png'),
                              
                'back': pygame.image.load('back.png'),
                'rePlay': pygame.image.load('replay.png'),
                
                'run': pygame.image.load('run3.png'),
                'mute2': pygame.image.load('skip.png'),
                'unMute2': pygame.image.load('play.png'),
                
                'home': pygame.image.load('home.png'),
                'help': pygame.image.load('help.png'),
                'options': pygame.image.load('settings.png'),

                'up': pygame.image.load('up.png'),
                'light': pygame.image.load('light.png'),
                'left': pygame.image.load('turn_left.png'),
                'right': pygame.image.load('turn_right.png'),
                'fun1': pygame.image.load('f1.png'),
                'fun2': pygame.image.load('f2.png'),
                'jump': pygame.image.load('jump0.png'),
                
                'BackGround': pygame.image.load('BackGround1.jpg'),
                'StartBackground': pygame.image.load('StartBackground.png'),
                
                #'done': pygame.image.load('finish.png'),
                'done': pygame.image.load('certificate.jpg'),
                'logo': pygame.image.load('ieee_logo.png'),
                'HOC': pygame.image.load('HOC.jpg'),
                
                
                'chFace': pygame.image.load('q.png'),
                'chBack': pygame.image.load('qq.png'),
                'chRight': pygame.image.load('qqq.png'),
                'chLeft': pygame.image.load('qqqq.png')

              }
    helpImageDic = {'0(1)': pygame.image.load('helpPic/0 (1).png'),
                    '0(2)': pygame.image.load('helpPic/0 (2).png'),
                    '0(3)': pygame.image.load('helpPic/0 (3).png'),
                    '0(4)': pygame.image.load('helpPic/0 (4).png'),
                    '0(5)': pygame.image.load('helpPic/0 (5).png'),
    
                    '1(1)': pygame.image.load('helpPic/1 (1).png'),
                    '1(2)': pygame.image.load('helpPic/1 (2).png'),
                    '1(3)': pygame.image.load('helpPic/1 (3).png'),
                    '1(4)': pygame.image.load('helpPic/1 (4).png'),
                    '1(5)': pygame.image.load('helpPic/1 (5).png'),

                    '2(1)': pygame.image.load('helpPic/2 (1).png'),
                    '2(2)': pygame.image.load('helpPic/2 (2).png'),
                    '2(3)': pygame.image.load('helpPic/2 (3).png'),
                    '2(4)': pygame.image.load('helpPic/2 (4).png'),
                    
                    '4(1)': pygame.image.load('helpPic/4 (1).png'),
    
                    '8(1)': pygame.image.load('helpPic/8 (1).png'),
                    '8(2)': pygame.image.load('helpPic/8 (2).png'),
                    '8(3)': pygame.image.load('helpPic/8 (3).png'),
                    '8(4)': pygame.image.load('helpPic/8 (4).png'),
                    '8(5)': pygame.image.load('helpPic/8 (5).png'),
                    '8(6)': pygame.image.load('helpPic/8 (6).png'),

                    '10(1)': pygame.image.load('helpPic/10 (1).png'),
                    '10(2)': pygame.image.load('helpPic/10 (2).png'),
                    '10(3)': pygame.image.load('helpPic/10 (3).png'),
                    '10(4)': pygame.image.load('helpPic/10 (4).png'),

                    '11(1)': pygame.image.load('helpPic/11 (1).png'),
                    '11(2)': pygame.image.load('helpPic/11 (2).png'),
                    '11(3)': pygame.image.load('helpPic/11 (3).png'),
    
                    '14(1)': pygame.image.load('helpPic/14 (1).png'),
                    '14(2)': pygame.image.load('helpPic/14 (2).png'),
                    '14(3)': pygame.image.load('helpPic/14 (3).png'),
                    '14(4)': pygame.image.load('helpPic/14 (4).png'),
                    
                    'palyingMethod': pygame.image.load('helpPic/palyingMethod.png')}
   
    while(True):
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                terminate()
                clock.tick(1)   
        pygame.display.update()
        sound(True , "first")
        startScreen1(True)
        

def gameHelp(currentLevel):
    
    if(currentLevel == 0 or currentLevel == 1 or currentLevel == 2 or currentLevel == 4 or currentLevel == 8 or currentLevel == 10 or currentLevel == 11 or currentLevel == 14 ):

        if(currentLevel == 0 or currentLevel == 1 or currentLevel == 2 ):
            current=currentLevel
            
        elif(currentLevel == 11 ):
            current= 6

        elif(currentLevel == 4 ):
            current= 3

        elif(currentLevel == 8 or currentLevel == 10  or currentLevel == 14 ):
            current=(currentLevel/2)

        
        helpFileA=open("helpFile.txt","r")
        lines=helpFileA.readlines()
        row=[]
        total=[]
        for line in lines:
            if(not line.startswith('\r') ):    
                row.append(line.rstrip())
            else:
                total.append(row)
                row=[]
                
        if(currentLevel==0):
            flag=1
            screenSurface.blit(helpImageDic['palyingMethod'],[0,0])
            pygame.display.update()
            while(1):
                for event in pygame.event.get():            
                    if event.type ==pygame.QUIT:
                        terminate()
                        clock.tick(1)
                    c=pygame.mouse.get_pressed()
                    if(c[0]==1):
                        flag=0
                        break
                if(flag==0):
                    break
        for x in range(len(total[current])):            
            flag=1
            screenSurface.blit(helpImageDic[ total[current][x] ],[0,0])
            pygame.display.update()
            while(1):
                for event in pygame.event.get():            
                    if event.type ==pygame.QUIT:
                        terminate()
                        clock.tick(1)
                    c=pygame.mouse.get_pressed()
                    if(c[0]==1):
                        flag=0
                        break
                if(flag==0):
                    break
    else:
        return None
    
    return

def sound(mode , screen):
    if(screen == "first"):
        if(mode== True):
            pygame.mixer.music.play(-1)
            button ('unMute',formMidWidth,formMidHeight,1.66)
            
        else:
            pygame.mixer.music.stop()
            button ('mute',formMidWidth,formMidHeight,1.66)
            
    else:
        if(mode== True):
            button ('unMute2',237,57,1)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()
            button ('mute2',237,57,1)
            
    pygame.display.update()

def cmd(currentLevel):
    
    screenSurface.blit(imageDic['up'],[138,665])
    screenSurface.blit(imageDic['light'],[223,665])
    #l&rB
    if(currentLevel>0):  
        screenSurface.blit(imageDic['left'],[308,665])
        screenSurface.blit(imageDic['right'],[393,665])
    #jumpB  
    if(currentLevel >1):
        screenSurface.blit(imageDic['left'],[308,665])
        screenSurface.blit(imageDic['right'],[393,665])
        screenSurface.blit(imageDic['jump'],[478,665])
    #f1B                
    if(currentLevel>=8):
        screenSurface.blit(imageDic['fun1'],[563,665])
    #f2B
    if((currentLevel>=11 and currentLevel<=13 ) or currentLevel==18 or currentLevel==19):
        screenSurface.blit(imageDic['fun2'],[648,665])


def cmdClick(cL,mousePosition,mouseClick,selectedFunction,mainCap,f1Cap,f2Cap):
    cursor=''
    mark=0
    if(cL==0):
        if ((mousePosition[0]>=142 and mousePosition[0]<=208)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='up'
                mark=1
        elif ((mousePosition[0]>=228 and mousePosition[0]<=294)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='light'
                mark=1

    elif(cL==1):
        if ((mousePosition[0]>=142 and mousePosition[0]<=208)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='up'
                mark=1
        elif ((mousePosition[0]>=228 and mousePosition[0]<=294)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='light'
                mark=1
        elif ((mousePosition[0]>=314 and mousePosition[0]<=380)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='left'
                mark=1
        elif ((mousePosition[0]>=400 and mousePosition[0]<=466)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='right'
                mark=1

    elif(cL > 1 and cL < 5):
        if ((mousePosition[0]>=142 and mousePosition[0]<=208)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='up'
                mark=1
        elif ((mousePosition[0]>=228 and mousePosition[0]<=294)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='light'
                mark=1
        elif ((mousePosition[0]>=314 and mousePosition[0]<=380)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='left'
                mark=1
        elif ((mousePosition[0]>=400 and mousePosition[0]<=466)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='right'
                mark=1
        elif ((mousePosition[0]>=486 and mousePosition[0]<=552)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='jump'
                mark=1
    elif(cL > 4 and cL < 8):
        if ((mousePosition[0]>=142 and mousePosition[0]<=208)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='up'
                mark=1
        elif ((mousePosition[0]>=228 and mousePosition[0]<=294)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='light'
                mark=1
        elif ((mousePosition[0]>=314 and mousePosition[0]<=380)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='left'
                mark=1
        elif ((mousePosition[0]>=400 and mousePosition[0]<=466)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='right'
                mark=1
        elif ((mousePosition[0]>=486 and mousePosition[0]<=552)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='jump'
                mark=1
        elif ((mousePosition[0]>=572 and mousePosition[0]<=638)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='fun1'
                mark=1

    elif(cL > 7):
        
        if ((mousePosition[0]>=142 and mousePosition[0]<=208)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='up'
                mark=1
        elif ((mousePosition[0]>=228 and mousePosition[0]<=294)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='light'
                mark=1
        elif ((mousePosition[0]>=314 and mousePosition[0]<=380)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='left'
                mark=1
        elif ((mousePosition[0]>=400 and mousePosition[0]<=466)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='right'
                mark=1
        elif ((mousePosition[0]>=486 and mousePosition[0]<=552)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='jump'
                mark=1
        elif ((mousePosition[0]>=572 and mousePosition[0]<=638)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='fun1'
                mark=1
        elif ((mousePosition[0]>=658 and mousePosition[0]<=724)and mousePosition[1] >=668 and mousePosition[1]<=735):
            if(mouseClick[0]== 1):
                cursor='fun2'
                mark=1
    if(mark):
        if(selectedFunction == "main" and (len(main)< mainCap)):
            
            main.append(cursor)
        elif(selectedFunction == "f1" and (len(f1)<f1Cap)):
            
            f1.append(cursor)
        elif(selectedFunction == "f2" and (len(f2)<f2Cap)):
            
            f2.append(cursor)

def drawCmdOnScreen(main):
    if(len(main)):
        num=-1
        col=(len(main)/4.0)
        if(col < 1 or col == 1):
            col=1
        elif(col > 1 and col <= 2 ):
            col=2
        elif(col > 2 and col <= 3):
            col=3
     
        for x in range(col):
            for y in range(4):
                num+=1
                if(num < len(main)):
                    screenSurface.blit(imageDic[main[num]],[855+(y*80),125+(x*80)])
                else:
                    break
        
    if(len(f1)):
        num1=-1
        col=(len(f1)/4.0)
        if(col < 1 or col == 1):
            col=1
        elif(col > 1 and col <= 2 ):
            col=2
            
        for x in range(col):
            for y in range(4):
                num1 +=1
                if(num1 < len(f1)):
                    screenSurface.blit(imageDic[f1[num1]],[855+(y*80),405+(x*80)])
                else:
                    break

    if(len(f2)):
        num2=-1
        col=(len(f2)/4.0)
        if(col < 1 or col == 1):
            col=1
        elif(col > 1 and col <= 2 ):
            col=2
            
        for x in range(col):
            for y in range(4):
                num2+=1
                if(num2 < len(f2)):
                    screenSurface.blit(imageDic[f2[num2]],[855+(y*80),605+(x*80)])
                else:
                    break

def drawFunctionsOnScreen(cL):
    #main
    pygame.draw.rect(screenSurface,white,[850,100,60,20])
    pygame.draw.rect(screenSurface,lightslategray,[850,120,325,245])
    printOnScreen("Main",maroon,852,126)
    mainCapacity=12
    f1Capacity=f2Capacity=8
    f1Status=False
    f2Status=False
    
    if(cL>=14 and cL<=19):
        pygame.draw.rect(screenSurface,silver,[855,125,75,75])
        mainCapacity=1
    #f1
    if((cL>=8 and cL <= 19 )  ):        
        pygame.draw.rect(screenSurface,white,[850,380,60,20])
        pygame.draw.rect(screenSurface,lightslategray,[850,400,325,165])
        printOnScreen("Fun1",maroon,852,406)
        f1Status=True
        
    if(cL == 14 or cL == 15):
        pygame.draw.rect(screenSurface,silver,[855,405,75,75])
        pygame.draw.rect(screenSurface,silver,[935,405,75,75])
        pygame.draw.rect(screenSurface,silver,[1015,405,75,75])
        f1Capacity=3
        f1Status=True

    #f2
    if((cL>=11 and cL <= 13) or cL == 18 or cL == 19):
        pygame.draw.rect(screenSurface,white,[850,580,60,20])
        pygame.draw.rect(screenSurface,lightslategray,[850,600,325,165])
        printOnScreen("Fun2",maroon,852,606)
        f2Status=True

    return mainCapacity,f1Capacity,f2Capacity,f1Status,f2Status


def gameCompleted():
    screenSurface.blit(imageDic['done'],[0,0])
    
def button (name,xCenter,yCenter,value):
    interfaceRect=imageDic[name].get_rect()
    interfaceRect.center=(xCenter,int((yCenter)*value))
    screenSurface.blit(imageDic[name],interfaceRect)
    pygame.display.update()

def buttonAction():
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

def printOnScreen(text,textColor,xPosition,yPosition):
    textSurf = basicFont.render(text, 1, textColor)
    textRect = textSurf.get_rect()
    textRect.bottomleft = (xPosition,yPosition)
    screenSurface.blit(textSurf, textRect)

def lightTheTile(levelMap,levelPositions,playerPosition,goalsLighting,numOfGoals):
    
    index=levelPositions.index((playerPosition))
    tileChar=levelMap[index][0]
    if(tileChar=='a' or tileChar=='b' or tileChar=='c' or tileChar=='d' or tileChar=='e'):
        if((tileChar,levelMap[index][1]) not in goalsLighting):
            goalsLighting.append((tileChar,levelMap[index][1]))
            numOfGoals-=1
            #print"if"
        else:
            goalsLighting.remove((tileChar,levelMap[index][1]))
            numOfGoals+=1
            #print"else"
    return numOfGoals

    
def startScreen1(status):
    global mode
    mode=status
    #screenSurface.blit(imageDic['k'],[0,0])
    screenSurface.fill(white)
    screenSurface.blit(imageDic['StartBackground'],[0,0])
    screenSurface.blit(imageDic['logo'],[502,20])
    screenSurface.blit(imageDic['HOC'],[500,235])
    
    button ('start',formMidWidth,formMidHeight,1.2)
    if(mode== True):
        button ('unMute',formMidWidth,formMidHeight,1.66)           
    else:
        button ('mute',formMidWidth,formMidHeight,1.66)
    
    
    while True:
    
        mousePosition=pygame.mouse.get_pos()
        mouseClick=pygame.mouse.get_pressed()

        for event in pygame.event.get():
            
            if event.type ==pygame.QUIT:
                terminate()
                clock.tick(1)
            
            #Exit    
            if event.type == pygame.KEYDOWN:
		    	if event.key == pygame.K_q:        
		            terminate()
		            clock.tick(1)

            #if ((mousePosition[0]>=450 and mousePosition[0]<=749)and mousePosition[1] >=415 and mousePosition[1]<=544):
            #if ((mousePosition[0]>=450 and mousePosition[0]<=749)and mousePosition[1] >=357 and mousePosition[1]<=484):
            if ((mousePosition[0]>=450 and mousePosition[0]<=749)and mousePosition[1] >=396 and mousePosition[1]<=522):
                if(mouseClick[0]== 1):
                    #print mode , "1"
                    startScreen(mode,0,True)
                    
            #elif ((mousePosition[0]>=566 and mousePosition[0]<=633)and mousePosition[1] >=630 and mousePosition[1]<=697):
            #elif ((mousePosition[0]>=566 and mousePosition[0]<=633)and mousePosition[1] >=548 and mousePosition[1]<=615):
            elif ((mousePosition[0]>=566 and mousePosition[0]<=633)and mousePosition[1] >=601 and mousePosition[1]<=667):
                if(mouseClick[0]== 1):
                    mode= not(mode)
                    sound(mode , "first")
                                                  
    
def startScreen(mode,currentLevel,helpMode):
    
    screenSurface.fill(white)
    
    replayMode=False
    
    backBtnShape=""
    
    #robotBosition=[(215,270),(215,270),(253,382),(73,426),(343,338),(118,448),(253,338),(163,426),(253,313),(73,424),(163,380),(253,292),(478,426),(433,404),(208,338),(208,362),(298,315),(73,402),(70,381),(70,426)]
    robotBosition=[(215,270),(215,270),(215,314),(35,358),(305,266),(80,380),(170, 292),(125,358),(215,246),(35,358),(125,314),(215,222),(440,356),(395,334),(170,268),(170,292),(260,244),(35,334),(35,310),(35,358)]
    playerPosition=robotBosition[currentLevel]
    
    if(helpMode):
        gameHelp(currentLevel)
    
        
    selectedFunction=''
    global main,f1,f2
    main=[]
    f1=  []
    f2=  []
    allCmds=[]
    levelMap=[]
    TilesPositionList=[]
    goals=[]
    ctr=1
    levelPositions=[]
    levelGround=[]
    charImg=['chFace','chLeft','chBack','chRight']
    crrentCharImg=0
    
    goalsLighting=[]
    numOfGoals=0
    if(currentLevel==7):
        imgDegree=90
    elif(currentLevel==12):
        imgDegree=180
    elif(currentLevel==13):
        imgDegree=180
    else:
        imgDegree=360
    while True:

        
        #screenSurface.blit(imageDic['background'],[0,0])
        screenSurface.blit(imageDic['BackGround'],[0,0])
        startX=215
        startY=270
        row=0
        
        for x in range(len(gameLevels[currentLevel])): 
            X=+startX
            Y=+startY          
            for char in gameLevels[currentLevel][row]:
                screenSurface.blit(imageDic[char],[X,Y])
                if(ctr):
                    #levelMap.append((char,(X,Y)))
                    #levelPositions.append((X,Y))
                    levelGround.append(char)
                    if(char=='1' or char=='a' or char=='v' or char==' ' or char=='-'):
                        levelPositions.append((X,Y))
                        levelMap.append((char,(X,Y)))
                    elif(char=='2' or char=='b' or char=='w'):
                        levelPositions.append((X,Y-24))
                        levelMap.append((char,(X,Y-24)))
                    elif(char=='3' or char=='c' or char=='x'):
                        levelPositions.append((X,Y-48))
                        levelMap.append((char,(X,Y-48)))
                    elif(char=='4' or char=='d' or char=='y'):
                        levelPositions.append((X,Y-72))
                        levelMap.append((char,(X,Y-72)))
                    elif(char=='5' or char=='e' or char=='z'):
                        levelPositions.append((X,Y-96))
                        levelMap.append((char,(X,Y-96)))

                    if(char=='a' or char=='b' or char=='c' or char=='d' or char=='e' ):
                        numOfGoals+=1
                    
                        
                    if((char != ' ') and (char != '-')):
                        TilesPositionList.append((X,Y))
                    if(char=='a' or char=='b' or char=='c' or char=='d' or char=='e' ):
                        goals.append((X,Y))
                    
                '''
                if ( X == playerPosition[0] ):
                    screenSurface.blit(imageDic['boy'],[playerPosition[0],playerPosition[1] ])
                    pygame.display.update()
                    print "YES"
                '''
                X+=45
                Y+=22                
            row+=1    
            startX-=45
            startY+=22
        ctr=0    
        mainCap,f1Cap,f2Cap,f1mode,f2mode=drawFunctionsOnScreen(currentLevel)
        

        if(currentLevel==0):
            backBtnShape='home'
        else:
            backBtnShape='back'

        if(goalsLighting!=[]):
            for goal in goalsLighting:
                screenSurface.blit(imageDic['l'],goal[1])
        
        screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])
        screenSurface.blit(imageDic[backBtnShape],[20,20])
        screenSurface.blit(imageDic['rePlay'],[110,20])

        screenSurface.blit(imageDic['run'],[920,20])
        screenSurface.blit(imageDic['help'],[1010,20])
        screenSurface.blit(imageDic['options'],[1100,20])
        
        drawCmdOnScreen(main)

        #cmd
        cmd(currentLevel)
        
        
        if(mode== True):
            button ('unMute2',237,57,1)            
        else:
            button ('mute2',237,57,1)
            
        if(replayMode== True):
            startScreen(mode,currentLevel,False)
        
        mousePosition=pygame.mouse.get_pos()
        mouseClick=pygame.mouse.get_pressed()
        
        pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type ==pygame.QUIT:
                terminate()
                clock.tick(1)
                
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if((playerPosition[0]-45 , playerPosition[1]-22)  in TilesPositionList ):        
                        playerPosition=(playerPosition[0]-45,playerPosition[1]-22)
                        screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])
                        
                elif event.key == pygame.K_DOWN:
                    if((playerPosition[0]+45 , playerPosition[1]+22)  in TilesPositionList ):    
                        playerPosition=(playerPosition[0]+45,playerPosition[1]+22)
                        screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])
                         
                    
                elif event.key == pygame.K_LEFT:
                    if((playerPosition[0]-45 , playerPosition[1]+22)  in TilesPositionList ): 
                        playerPosition=(playerPosition[0]-45,playerPosition[1]+22)
                        screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])
                        
                elif event.key == pygame.K_RIGHT:                    
                    if((playerPosition[0]+45 , playerPosition[1]-22)  in TilesPositionList ): 
                        playerPosition=(playerPosition[0]+45,playerPosition[1]-22)
                        screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])
                #Jump 
                elif event.key == pygame.K_SPACE:                    
                    playerPosition=(playerPosition[0],playerPosition[1]-24)
                    playerPosition=(playerPosition[0]-45,playerPosition[1]-22)
                    screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])
                #Cancel Jump
                elif event.key == pygame.K_a:                    
                    playerPosition=(playerPosition[0],playerPosition[1]+24)
                    playerPosition=(playerPosition[0]+45,playerPosition[1]+22)
                    screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])

                elif event.key == pygame.K_n:
                    
                    if(currentLevel<len(gameLevels)-1):
                        
                        currentLevel+=1
                        gameHelp(currentLevel)
                        playerPosition=robotBosition[currentLevel]
                        #screenSurface.blit(imageDic['background'],[0,0])
                        startScreen(mode,currentLevel,False)
                    else:
                        print("159159159")
                #LIGHT       
                elif event.key == pygame.K_l:
                    tileChar=levelMap[index][0]
                    if(tileChar=='a' or tileChar=='b' or tileChar=='c' or tileChar=='d' or tileChar=='e'):
                        if((tileChar,levelMap[index][1]) not in goalsLighting):
                            goalsLighting.append((tileChar,levelMap[index][1]))
                            numOfGoals-=1
                            #print"if"
                        else:
                            goalsLighting.remove((tileChar,levelMap[index][1]))
                            numOfGoals+=1
                            #print"else"
                    #print"numOfGoals",numOfGoals
                    
                    
                #JUMP     
                elif event.key == pygame.K_j:
                    index=levelPositions.index((playerPosition))
                    tilesList=[['1','a','v'],['2','b','w'],['3','c','x'],['4','d','y'],['5','e','z']]
                    if(imgDegree == 0 or imgDegree == 360 ):
                        #***check*** if the diff detween current tiles and the next equal 1.
                        if((index+1 < len(levelMap)) and (((index+1)%(len(levelMap)/row))!=0)):#len(levelMap)/row):
                            nextTile =levelMap[index+1][0]
                            currentTile =levelMap[index][0]
                            nextTileHight=-2
                            currentTileHight=-1
                            for element in tilesList :
                                if currentTile in element:
                                    currentTileHight=tilesList.index(element)
                                if nextTile in element:
                                    nextTileHight=tilesList.index(element)
                            #print currentTileHight,nextTileHight
                            if(abs(nextTileHight-currentTileHight)==1):
                                #print "possible with condition"
                                playerPosition=levelMap[index+1][1]
                            else:
                                print ('not possible')
                        else:
                            print ('not possible')
                            
                        print ('forward')
                        
                        
                    elif(imgDegree == 180):
                        if((index-1 >= 0) and (((index)%(len(levelMap)/row))!=0)):#len(levelMap)/row):
                            nextTile =levelMap[index-1][0]
                            currentTile =levelMap[index][0]
                            nextTileHight=-2
                            currentTileHight=-1
                            for element in tilesList :
                                if currentTile in element:
                                    currentTileHight=tilesList.index(element)
                                if nextTile in element:
                                    nextTileHight=tilesList.index(element)
                            #print currentTileHight,nextTileHight
                            if(abs(nextTileHight-currentTileHight)==1):
                                #print "possible with condition"
                                playerPosition=levelMap[index-1][1]
                            else:
                                print ('not possible')
                        else:
                            print ('not possible')

                        print ('backword')
                        
                        
                    elif(imgDegree == 90 ):
                        if((index-(len(levelMap)/row))>=0 ):
                            nextTile =levelMap[(index-(len(levelMap)/row))][0]
                            currentTile =levelMap[index][0]
                            nextTileHight=-2
                            currentTileHight=-1
                            for element in tilesList :
                                if currentTile in element:
                                    currentTileHight=tilesList.index(element)
                                if nextTile in element:
                                    nextTileHight=tilesList.index(element)
                            #print currentTileHight,nextTileHight
                            if(abs(nextTileHight-currentTileHight)==1):
                                #print "possible with condition"
                                playerPosition=levelMap[(index-(len(levelMap)/row))][1]
                            else:
                                print ('not possible')
                        else:
                            print ('not possible')
                            
                        print ('right')
                            
                    
                    elif(imgDegree == 270 ):
                        if((index+(len(levelMap)/row))< len(levelMap) ):
                            nextTile =levelMap[(index+(len(levelMap)/row))][0]
                            currentTile =levelMap[index][0]
                            nextTileHight=-2
                            currentTileHight=-1
                            for element in tilesList :
                                if currentTile in element:
                                    currentTileHight=tilesList.index(element)
                                if nextTile in element:
                                    nextTileHight=tilesList.index(element)
                            #print currentTileHight,nextTileHight
                            if(abs(nextTileHight-currentTileHight)==1):
                                #print "possible with condition"
                                playerPosition=levelMap[(index+(len(levelMap)/row))][1]
                            else:
                                print ('not possible')
                        else:
                            print ('not possible')

                            print ('left')
                            
                     

                #left
                elif event.key == pygame.K_f:
                    if(imgDegree==0):
                        imgDegree=360
                    imgDegree-=90
                    #print imgDegree
              
                #right
                elif event.key == pygame.K_r:
                    if(imgDegree==360):
                        imgDegree=0
                    imgDegree+=90 
                    #print imgDegree
                    
                #charImg         
                elif event.key == pygame.K_b:
                    
                    if(currentLevel>0):
                        
                        currentLevel-=1
                        playerPosition=robotBosition[currentLevel]
                        #screenSurface.blit(imageDic['background'],[0,0])
                        startScreen(mode,currentLevel,False)

                elif event.key == pygame.K_q:
                    pass
                    #print playerPosition[0],playerPosition[1]
                #print playerPosition[0],playerPosition[1]
                pygame.display.update()
                
            
            #back
            elif ((mousePosition[0]>=23 and mousePosition[0]<=92)and mousePosition[1] >=23 and mousePosition[1]<=93):
                if(mouseClick[0]== 1):
                    if(currentLevel==0):
                        startScreen1(mode)
                    else:
                        currentLevel=currentLevel-1
                        playerPosition=robotBosition[currentLevel]
                        startScreen(mode,currentLevel,False)
                        

            #replay
            elif ((mousePosition[0]>=113 and mousePosition[0]<=182)and mousePosition[1] >=23 and mousePosition[1]<=93):
                if(mouseClick[0]== 1):
                    replayMode= not(replayMode)
                    

            #sound
            if ((mousePosition[0]>=203 and mousePosition[0]<=272)and mousePosition[1] >=23 and mousePosition[1]<=93):
                if(mouseClick[0]== 1):
                    mode= not(mode)
                    sound(mode , "second")
                     
            #run       
            elif ((mousePosition[0]>=922 and mousePosition[0]<=992)and mousePosition[1] >=23 and mousePosition[1]<=93):
                if(mouseClick[0]== 1):
                    #print "run_ClicK"
                    newF1=[]
                    newF2=[]
                    newF1=f1
                    newF2=f2
                    if('fun1' in f1):
                        l=[]
                        newF1=[]
                        for elem in f1:
                            if(elem != 'fun1'):
                                l.append(elem)
                            else:
                                newF1=l*6
                        #print "f1= ",newF1
                    if('fun2' in f2):
                        l2=[]
                        newF2=[]
                        for elem in f2:
                            if(elem != 'fun2'):
                                l2.append(elem)
                            else:
                                newF2=l2*6
                        #print "f2= ",newF2
                    allCmds=[]
                    for element in main:
                        if(element == "fun1"):
                            allCmds.extend(newF1)
                        elif(element == "fun2"):
                            allCmds.extend(newF2)
                        else:
                           allCmds.append(element)
                    allCmds2=[]
                    for e in allCmds:
                        if(e == "fun1"):
                            allCmds2.extend(newF1)
                        elif(e == "fun2"):
                            allCmds2.extend(newF2)
                        else:
                            allCmds2.append(e)
                           
                    #print "allCmds: ",allCmds2
                    #movement(main)
                    for cMd in allCmds2:
                        if(cMd=='up'):
                            index=levelPositions.index((playerPosition))
                            tilesList=[['1','a','v'],['2','b','w'],['3','c','x'],['4','d','y'],['5','e','z']]
                            if(imgDegree == 0 or imgDegree == 360 ):
                                #***check*** if the diff detween current tiles and the next equal 1.
                                if((index+1 < len(levelMap)) and (((index+1)%(len(levelMap)/row))!=0)):#len(levelMap)/row):
                                    nextTile =levelMap[index+1][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==0):
                                        #print "possible move with condition"
                                        playerPosition=levelMap[index+1][1]
                                    else:
                                        print ('not possible move')
                                else:
                                    print ('not possible move')
                                    
                                print ('forward')
                                
                                
                            elif(imgDegree == 180):
                                if((index-1 >= 0) and (((index)%(len(levelMap)/row))!=0)):#len(levelMap)/row):
                                    nextTile =levelMap[index-1][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==0):
                                        #print "possible move with condition"
                                        playerPosition=levelMap[index-1][1]
                                    else:
                                        print ('not possible move')
                                else:
                                    print ('not possible move')

                                print ('backword')
                                
                                
                            elif(imgDegree == 90 ):
                                if((index-(len(levelMap)/row))>=0 ):
                                    nextTile =levelMap[(index-(len(levelMap)/row))][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==0):
                                        #print "possible move with condition"
                                        playerPosition=levelMap[(index-(len(levelMap)/row))][1]
                                    else:
                                        print ('not possible move')
                                else:
                                    print ('not possible move')
                                    
                                print ('right')
                                    
                            
                            elif(imgDegree == 270 ):
                                if((index+(len(levelMap)/row))< len(levelMap) ):
                                    nextTile =levelMap[(index+(len(levelMap)/row))][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==0):
                                        #print "possible move with condition"
                                        playerPosition=levelMap[(index+(len(levelMap)/row))][1]
                                    else:
                                        print ('not possible move')
                                else:
                                    print ('not possible move')

                                    print ('left')
                        
                        elif(cMd == 'left'):
                            if(imgDegree==360):
                                imgDegree=0
                            imgDegree+=90 
                            #print imgDegree
                            
                        elif(cMd == 'right'):
                            if(imgDegree==0):
                                imgDegree=360
                            imgDegree-=90
                            #print imgDegree
                            
                        elif(cMd == 'light'):
                            #print "i'm in light"
                            numOfGoals=lightTheTile(levelMap,levelPositions,playerPosition,goalsLighting,numOfGoals)
                            #if(numOfGoals==0):
                                #break
                
                        elif(cMd == 'jump'):
                            index=levelPositions.index((playerPosition))
                            tilesList=[['1','a','v'],['2','b','w'],['3','c','x'],['4','d','y'],['5','e','z']]
                            if(imgDegree == 0 or imgDegree == 360 ):
                                #***check*** if the diff detween current tiles and the next equal 1.
                                if((index+1 < len(levelMap)) and (((index+1)%(len(levelMap)/row))!=0)):#len(levelMap)/row):
                                    nextTile =levelMap[index+1][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==1):
                                        #print "possible with condition"
                                        playerPosition=levelMap[index+1][1]
                                    else:
                                        print ('not possible')
                                else:
                                    print ('not possible')
                                    
                                print ('forward')
                                
                                
                            elif(imgDegree == 180):
                                if((index-1 >= 0) and (((index)%(len(levelMap)/row))!=0)):#len(levelMap)/row):
                                    nextTile =levelMap[index-1][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==1):
                                        #print "possible with condition"
                                        playerPosition=levelMap[index-1][1]
                                    else:
                                        print ('not possible')
                                else:
                                    print ('not possible')

                                print ('backword')
                                
                                
                            elif(imgDegree == 90 ):
                                if((index-(len(levelMap)/row))>=0 ):
                                    nextTile =levelMap[(index-(len(levelMap)/row))][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==1):
                                        #print "possible with condition"
                                        playerPosition=levelMap[(index-(len(levelMap)/row))][1]
                                    else:
                                        print ('not possible')
                                else:
                                    print ('not possible')
                                    
                                print ('right')
                                    
                            
                            elif(imgDegree == 270 ):
                                if((index+(len(levelMap)/row))< len(levelMap) ):
                                    nextTile =levelMap[(index+(len(levelMap)/row))][0]
                                    currentTile =levelMap[index][0]
                                    nextTileHight=-2
                                    currentTileHight=-1
                                    for element in tilesList :
                                        if currentTile in element:
                                            currentTileHight=tilesList.index(element)
                                        if nextTile in element:
                                            nextTileHight=tilesList.index(element)
                                    #print currentTileHight,nextTileHight
                                    if(abs(nextTileHight-currentTileHight)==1):
                                        #print "possible with condition"
                                        playerPosition=levelMap[(index+(len(levelMap)/row))][1]
                                    else:
                                        print ('not possible')
                                else:
                                    print ('not possible')

                                    print ('left')
                        if(imgDegree==0 or imgDegree==360 ):
                            crrentCharImg=0
                        elif(imgDegree==270):
                            crrentCharImg=1
                        elif(imgDegree==180):
                            crrentCharImg=2
                        elif(imgDegree==90):
                            crrentCharImg=3

                        #draw
                        #print 'in',cMd
                        #screenSurface.blit(imageDic['background'],[0,0])
                        screenSurface.blit(imageDic['BackGround'],[0,0])
                        startX=215
                        startY=270
                        row=0

                        for x in range(len(gameLevels[currentLevel])): 
                            X=+startX
                            Y=+startY          
                            for char in gameLevels[currentLevel][row]:
                                screenSurface.blit(imageDic[char],[X,Y])
                                if(goalsLighting!=[]):
                                    for goal in goalsLighting:
                                        if((char=='a' and goal[1]==(X,Y)) or (char=='b' and goal[1]==(X,Y-24)) or(char=='c' and goal[1]==(X,Y-48)) or(char=='d' and goal[1]==(X,Y-72)) or(char=='e' and goal[1]==(X,Y-96))):
                                            screenSurface.blit(imageDic['l'],goal[1])
                                X+=45
                                Y+=22                
                            row+=1    
                            startX-=45
                            startY+=22
                        ctr=0    
                        mainCap,f1Cap,f2Cap,f1mode,f2mode=drawFunctionsOnScreen(currentLevel)

                        if(currentLevel==0):
                            backBtnShape='home'
                        else:
                            backBtnShape='back'
                        '''

                        if(goalsLighting!=[]):
                            for goal in goalsLighting:
                                screenSurface.blit(imageDic['l'],goal[1])
                        '''

                        screenSurface.blit(imageDic[charImg[crrentCharImg]],[playerPosition[0],playerPosition[1] ])
                        screenSurface.blit(imageDic[backBtnShape],[20,20])
                        screenSurface.blit(imageDic['rePlay'],[110,20])

                        screenSurface.blit(imageDic['run'],[920,20])
                        screenSurface.blit(imageDic['help'],[1010,20])
                        screenSurface.blit(imageDic['options'],[1100,20])

                        drawCmdOnScreen(main)

                        #cmd
                        cmd(currentLevel)


                        if(mode== True):
                            button ('unMute2',237,57,1)            
                        else:
                            button ('mute2',237,57,1)
                            
                        if(replayMode== True):
                            startScreen(mode,currentLevel,False)

                        mousePosition=pygame.mouse.get_pos()
                        mouseClick=pygame.mouse.get_pressed()
                        
                        #pygame.display.update()
                        pygame.time.delay(400)
                        #pygame.time.set_timer(1, 500) 
                        #time.sleep(3)
                        if(numOfGoals == 0):
                            break
                    if(numOfGoals == 0):
                        if(currentLevel<len(gameLevels)-1):
                            currentLevel+=1
                            gameHelp(currentLevel)
                            playerPosition=robotBosition[currentLevel]
                            startScreen(mode,currentLevel,False)
                            
                        else:
                            #print"Show Final Screen "
                            sign=1
                            screenSurface.blit(imageDic['done'],[57,0])
                            pygame.display.update()
                            while(1):
                                for event in pygame.event.get():            
                                    if event.type ==pygame.QUIT:
                                        terminate()
                                        clock.tick(1)
                                '''
                                    c=pygame.mouse.get_pressed()
                                    if(c[0]==1):
                                        sign=0
                                        break
                                if(sign==0):
                                    break
                                '''
                        
                        
                    else:
                        playerPosition=robotBosition[currentLevel]
                        goalsLighting=[]
                        imgDegree=0
                        numOfGoals=len(goals)
               
            #help
            elif ((mousePosition[0]>=1012 and mousePosition[0]<=1082)and mousePosition[1] >=23 and mousePosition[1]<=93):
                if(mouseClick[0]== 1):
                    gameHelp(currentLevel)
            #settiongs
            elif ((mousePosition[0]>=1102 and mousePosition[0]<=1172)and mousePosition[1] >=23 and mousePosition[1]<=93):
                if(mouseClick[0]== 1):
                    print ("settings_ClicK")
            
            #choose function
            elif ((mousePosition[0]>=851 and mousePosition[0]<=1174)and mousePosition[1] >=121 and mousePosition[1]<=364):
                if(mouseClick[0]== 1):
                    selectedFunction="main"
                elif(mouseClick[2]== 1 and len(main)):
                    main.pop()
                    
                        
            elif ((mousePosition[0]>=851 and mousePosition[0]<=1174)and mousePosition[1] >=401 and mousePosition[1]<=564):
                if(mouseClick[0]== 1 and f1mode):
                    selectedFunction= "f1"
                elif(mouseClick[2]== 1 and len(f1) ):
                    f1.pop()
                    
            elif ((mousePosition[0]>=851 and mousePosition[0]<=1174)and mousePosition[1] >=601 and mousePosition[1]<=764):
                if(mouseClick[0]== 1 and f2mode):
                    selectedFunction= "f2"
                elif(mouseClick[2]== 1 and len(f2)):
                    f2.pop()

            

            #Commands click
            cmdClick(currentLevel,mousePosition,mouseClick,selectedFunction,mainCap,f1Cap,f2Cap)
            #print main,f1,f2
            if(imgDegree==0 or imgDegree==360 ):
                crrentCharImg=0
            elif(imgDegree==270):
                crrentCharImg=1
            elif(imgDegree==180):
                crrentCharImg=2
            elif(imgDegree==90):
                crrentCharImg=3
            
def terminate():
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()

