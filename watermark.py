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
        
        print ('hell -', filename)

        # folder
        gambar = namee
        (filename, file_extension) = os.path.splitext(gambar)

        # mengambil gambar
        folder = 'photo/'
        image = Image.open(folder + filename + file_extension)
        imageWidth = image.width
        imageHeight = image.height

        # mengambil logo
        logo = Image.open('watermark/logo-entmart-20.png')

        logoWidth = logo.width
        logoHeight = logo.height

        # merisize logo 50% berdasarkan ukuran gambar
        rl_width = int(imageWidth * 50 / 100)
        rl_height = int(imageHeight * 7 / 100)

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


            