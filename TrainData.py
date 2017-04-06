from PIL import Image
import numpy as np

def TrainData():
    numberArrayExamples = open('train.txt','w')
    numbersWeHave = range(0,10)
    for eachNum in numbersWeHave:
        for furtherNum in numbersWeHave:
            imgFilePath = 'pic\\'+str(eachNum)+'.'+str(furtherNum)+'.png'
            print(imgFilePath)
            image = Image.open(imgFilePath)
            imagearray = str(np.array(image).tolist())
            lineToWrite = str(eachNum)+'::'+imagearray+'\n'
            numberArrayExamples.write(lineToWrite)
            
TrainData()