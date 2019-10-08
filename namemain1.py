import os, sys
#import Image
import string # have to compulsory import string module for executing string methods like string.split

fileName = 'balablahblahabalal'
def convertFile(fileName):
    splitName = string.split(fileName, "_")
    endName = splitName[2]
    splitTwo = string.split(endName, ".")
    userFolder = splitTwo[0]

    #imageFile = "/var/www/uploads/tmp/"+fileName
    

    print fileName     # (rest of the script)
    print userFolder
    return


if __name__ == '__main__':
    filename = sys.argv[1]
    convertFile(filename)
# C:| ....python jurassic_park_steven.io gives out put jurassic_park_steven.io and steven