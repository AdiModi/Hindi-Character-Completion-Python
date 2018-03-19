import cv2, numpy as np, os, random, src.ProjectParameters as pp

inkDropFilePaths = os.listdir(pp.inkDropDirectoryPath)
inkDropImages = []
for inkDropFilePath in inkDropFilePaths:

    # Reading filters from files
    image = cv2.imread(os.path.join(pp.inkDropDirectoryPath, inkDropFilePath), cv2.IMREAD_GRAYSCALE)

    # Uncomment the following lines to resize the images
    # image = cv2.resize(image, (pp.ImageNoiseParameters["InkDrop"]["filterSize"][0], pp.ImageNoiseParameters["InkDrop"]["filterSize"][1]), image)
    # cv2.imwrite(os.path.join(pp.inkDropDirectoryPath, inkDropFilePath), image)

    inkDropImages.append(image)

def inkDrop(image):

    # Taking Image Size
    imageShape = image.shape

    # Selecting Filter and Rotating it
    inkDropImage = inkDropImages[random.randint(0, len(inkDropImages)-1)]
    M = cv2.getRotationMatrix2D((random.randint(0, imageShape[0] - 1), random.randint(0, imageShape[1] - 1)), random.randint(0, 360), random.uniform(0.7, 1))
    inkDropImage = cv2.warpAffine(inkDropImage, M, (imageShape[0], imageShape[1]))

    image = cv2.add(image, inkDropImage)
    return image

# for i in range(0, 20):
#     image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
#     cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i+1) + '.png',
#                 inkDrop(image=image))