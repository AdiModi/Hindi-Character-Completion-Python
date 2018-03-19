import glob
import os
import cv2
import numpy as np, math
import tqdm
import random

untouchedDatasetDirectoryPath = ''
# D:\Codes\Python\Major Project\resrc\Untouched\test\0
corruptedDatasetDirectoryPath = ''
# D:\Codes\Python\Major Project\resrc\Corrupted\test\0

def corruptImagesFromDirectoryRecursively(sourceDirectoryPath='',
                                          destinationDirectoryPath=''):
    imagePaths = glob.glob(os.path.join(sourceDirectoryPath, '*.png'))
    totalImages = len(imagePaths)

    print('Corrupting images from: \'' + sourceDirectoryPath + '\'\nAnd Saving it to: \'' + destinationDirectoryPath + '\'')
    progressBar = tqdm.tqdm(total=totalImages, dynamic_ncols=False, unit=' Images', initial=0, ncols=100)

    for imagePath in imagePaths:
        imageName = imagePath[imagePath.rindex(os.sep) + 1:]
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        refillcolor = random.randint(0, 10)
        if refillcolor>5:
            refillcolor=255
        else:
            refillcolor=0
        corruptedImage = noiseFunction()
        cv2.imwrite(os.path.join(destinationDirectoryPath, imageName), corruptedImage)
        progressBar.update(1)

    progressBar.close()

    '''
    for item in os.listdir(sourceDirectoryPath):
        if os.path.isdir(os.path.join(sourceDirectoryPath, item)):
            os.mkdir(os.path.join(destinationDirectoryPath, item))
            corruptImagesFromDirectoryRecursively(os.path.join(sourceDirectoryPath, item),
                                                  os.path.join(destinationDirectoryPath, item))
    '''

untouchedDatasetDirectoryPath = os.path.join('D:'.join(os.sep), 'Codes', 'Python', 'Major Project', 'resrc', 'Untouched')
# untouchedDatasetDirectoryPath = input('Please enter the root directory path: ')
while True:
    if not os.path.isdir(untouchedDatasetDirectoryPath):
        print(untouchedDatasetDirectoryPath)
        print('Directory path does not exist!\n')
        untouchedDatasetDirectoryPath = input('Please enter a valid directory path: ')
    else:
        break

corruptedDatasetDirectoryPath = os.path.join('D:'.join(os.sep), 'Codes', 'Python', 'Major Project', 'resrc', 'Corrupted')

# corruptedDatasetDirectoryPath = input('Please enter the root directory path: ')
if not os.path.isdir(corruptedDatasetDirectoryPath):
    os.mkdir(corruptedDatasetDirectoryPath)

corruptImagesFromDirectoryRecursively(sourceDirectoryPath=untouchedDatasetDirectoryPath,
                                      destinationDirectoryPath=corruptedDatasetDirectoryPath)