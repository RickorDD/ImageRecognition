from PIL import Image
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('C:\\daten\\ki\pic\\numb\\train.txt','r').read()
    loadExamps = loadExamps.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print(str(e))
                
    #print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    #print(x[7])
    
    graphX = []
    graphY = []


    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])



    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)
    
    ax1.axis('off')
    ax1.imshow(iar, cmap='gray')
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    ax2.set_xlim([-1,10])

    plt.show()
    
whatNumIsThis('pic\\test.png')