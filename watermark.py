#!/usr/bin/python
# coder Irfannur Diah - irfnrdh.com

import os
import sys

from PIL import Image

def getListOfFiles(dirName):

    # create a list of file and sub directories
    # names in the given directory

    listOfFile = os.listdir(dirName)
    allFiles = list()

    # Iterate over all the entries

    for entry in listOfFile:

        # Create full path

        fullPath = os.path.join(dirName, entry)

        # If entry is a directory then get the list of files in this directory

        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def main():
    dirName = 'photo'

    # Get the list of all files in directory tree at given path

    listOfFiles = getListOfFiles(dirName)

    # Print the files

    for elem in listOfFiles:
        namee = os.path.basename(elem)
        (filename, file_extension) = os.path.splitext(namee)
        
        print ('Detection -', elem)

        if file_extension == '.jpg' or file_extension == '.png' :
            # mengambil gambar
            image = Image.open(elem)
        
            imageWidth = image.width
            imageHeight = image.height

            # folder
            gambar = namee
            (filename, file_extension) = os.path.splitext(gambar)

            # mengambil logo
            logo = Image.open('watermark/logo-entmart-20.png')

            logoWidth = logo.width
            logoHeight = logo.height

            #mendapatkan potrait, landscape dan squere dan merisize 50%
            hasil = imageHeight- imageWidth 
            
            if hasil == 0:
                rl_width = int(imageWidth * 50 / 100)
                rl_height = int(imageHeight * 50 / 100)
                print("squere")

            #masih perlu optimasi
            elif hasil >= 0 and hasil <= 50 :
                rl_width = int(imageWidth * 50 / 100)
                rl_height = int(imageHeight * 50 / 100)
                print("Antara Squere dan Potrait")
            elif hasil >= 50 :   
                rl_width = int(imageWidth * 50 / 100)
                rl_height = int(imageHeight * 35 / 100)
                print("Potrait")

            #masih perlu optimasi
            elif hasil <= 0 and hasil <=(-50):
                rl_width = int(imageWidth * 30 / 100)
                rl_height = int(imageHeight * 50 / 100)
                print("Antara Potrait dan landscape")
            elif hasil <=(-50):
                rl_width = int(imageWidth * 30 / 100)
                rl_height = int(imageHeight * 50 / 100)
                print("landscape")

            
            # Resize gambar
            logoh = logo.resize((rl_width, rl_height), Image.ANTIALIAS)

            # Posisi Tengah
            position = (int((imageWidth - rl_width) / 2), int((imageHeight
                        - rl_height) / 2))

            # Top Left  ....-> (0, 0)
            # Top Right ....-> (imageWidth - logoWidth, 0)
            # Bottom Left ....-> (0, imageHeight - logoHeight)
            # Bottom Right  -> (imageWidth - logoWidth, imageHeight - logoHeight)

            # menyimpan gambar

            image.paste(logoh, position, logoh)
            image.save('output/' + gambar)


if __name__ == '__main__':
    main()
    print("Mantull")


            
