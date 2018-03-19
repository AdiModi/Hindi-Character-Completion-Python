import cv2, numpy as np, random
from src import ProjectParameters as pp

def erasedRectangleHard(image, shape=(1, 1), refillColor=0):

    if shape[0] == 0 or shape[1] == 0:
        return image

    # Taking Image Size
    imageShape = image.shape

    # Calculating the start of the rectangle
    startIndex = (random.randint(0, imageShape[0] - shape[0]), random.randint(0, imageShape[1] - shape[1]))

    # Creating the blend matrix
    blendMatrix = np.zeros((imageShape[0], imageShape[1]))
    blendMatrix[startIndex[0]: startIndex[0] + shape[0], startIndex[1]: startIndex[1] + shape[1]] = 1

    # Rotating the blend matrix
    M = cv2.getRotationMatrix2D((int((startIndex[0] + shape[0])/2), int((startIndex[0] + shape[1])/2)), random.randint(0, 360), random.uniform(0.7, 1))
    blendMatrix = cv2.warpAffine(blendMatrix, M, (imageShape[1], imageShape[1]))

    image=np.multiply(image, 1 - blendMatrix) + np.multiply(refillColor, blendMatrix)
    return image

# for i in range(0, 20):
#     image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
#     cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i+1) + '.png',
#                 erasedRectangleHard(image=image,
#                                     shape=(random.randint(pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthXLimits"][0], pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthXLimits"][1]), random.randint(pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthYLimits"][0], pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthYLimits"][1])),
#                                     refillColor=np.random.choice(a=pp.ImageNoiseParameters["ErasedRectangleHard"]["refillColors"], size=1, p=pp.ImageNoiseParameters["ErasedRectangleHard"][ "refillColorProbabilities"])[0]))