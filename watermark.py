#!/usr/bin/python
# coder Irfannur Diah - irfnrdh.com

# rilis  1 - 21 Okt 19
# Update 2 - 19 Mar 20

import os
import sys

from PIL import Image

# mendapatkan semua file dalam folder


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

# menambahkan watermark


def watermark(gambar, watermark, posisi, output):
    gambar = Image.open(gambar)
    watermark = Image.open(watermark)

    gambar.paste(watermark, posisi, mask=watermark)
    gambar.show()
    gambar.save(output)


def main(folder, watermark):
    dirName = folder
    listOfFiles = getListOfFiles(dirName)

    for elem in listOfFiles:
        namee = os.path.basename(elem)
        (filename, file_extension) = os.path.splitext(namee)

        if file_extension == '.jpg' or file_extension == '.png':

            print('Detection - ', elem)

            # mengambil gambar
            image = Image.open(elem)

            imageWidth = image.width
            imageHeight = image.height

            # folder
            gambar = namee
            (filename, file_extension) = os.path.splitext(gambar)

            # mengambil logo
            logo = Image.open(watermark)

            logoWidth = logo.width
            logoHeight = logo.height

            # mendapatkan potrait, landscape dan squere dan merisize 50%
            hasil = imageHeight - imageWidth

            if hasil > 0:
                # tergantung ukuran watermark
                rl_width = int(imageWidth * 50 / 100)
                rl_height = int(imageHeight * 6 / 100)
                print("Detection -  Potrait")
            elif hasil < 0:
                rl_width = int(imageWidth * 35 / 100)
                rl_height = int(imageHeight * 8 / 100)
                print("Detection -  Landscape")
            if hasil == 0:
                rl_width = int(imageWidth * 50 / 100)
                rl_height = int(imageHeight * 50 / 100)
                print("Detection -  Squere")

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
    folder = 'photo'
    watermark = 'watermark/logo-entmart-20.png'
    main(folder, watermark)
