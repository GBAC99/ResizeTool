from PIL import Image
import os

#Method to resize an image when is needed, keeping it's aspect ratio
def resizeImage(im,newWidth): 
    w,h = im.size
    ratio = h/w 
    newHeight = int(ratio*newWidth)
    resImage = im.resize((newWidth,newHeight))
    return resImage


#Method to iterate inside of the folder to create the new assets
def transformImage():

    path = input("Write the name od the folder to process")

    newWidth = input("Declare the width to resize to")
    newHeigth = input("Declare the heigth to resize to")

    files = os.listdir(path)
    extension = 'png'
    imageOrderNum = 0
    for image in files:
        basePng = Image.new('RGBA',(newWidth,newHeigth),(0,0,0,0)) 
        ext = image.split(".")[-1]
        if ext in extension:
            im = Image.open(path+"/"+image)
            oWidth = im.size[0]
            if oWidth > basePng.size[0]:
                resIm = resizeImage(im,newWidth)
                if resIm.size[1] > basePng.size[1]:
                     
                    cropTimes = resIm.size[1]/basePng.size[1]  
                    cropTimes = int(cropTimes.__round__()) 
                    count = 0
                    while count < cropTimes-1: 
                        heightCrop = int((resIm.size[1]/cropTimes)*(count+1))
                        basePng.paste(resIm,(0,-(heightCrop)),resIm)
                        filePath = f"2dassets/new{image}_{imageOrderNum}.png"
                        basePng.save(filePath)

                        imageOrderNum += 1

                        count += 1 

                basePng.paste(resIm,(0,0),resIm)
                filePath = f"2dassets/new{image}_{imageOrderNum}.png"
                basePng.save(filePath)
                imageOrderNum += 1
            else:
                basePng.paste(im,(0,0),im)
                filePath = f"2dassets/new{image}_{imageOrderNum}.png"
                basePng.save(filePath)
                imageOrderNum += 1

transformImage()
 
