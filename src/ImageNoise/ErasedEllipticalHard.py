import cv2, numpy as np, random
from src import ProjectParameters as pp

def erasedEllipticalHard(image, axisShape=(1, 1), refillColor=0):

    imageShape = image.shape
    center = (random.randint(0, imageShape[0] - 1), random.randint(0, imageShape[1] - 1))
    blendMatrix = np.zeros((imageShape[0], imageShape[1]))

    y, x = np.ogrid[-center[0]:imageShape[0] - center[0], -center[1]:imageShape[1] - center[1]]
    booleanMask = ((x ** 2) / (axisShape[1] ** 2)) + ((y ** 2) / (axisShape[0] ** 2)) < 1
    blendMatrix[booleanMask] = 1

    M = cv2.getRotationMatrix2D((center[0], center[1]), random.randint(0, 360), 1)
    blendMatrix = cv2.warpAffine(blendMatrix, M, (imageShape[1], imageShape[0]))

    image = np.multiply(image, 1 - blendMatrix) + np.multiply(refillColor, blendMatrix)
    return image

for i in range(0, 20):
    image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i+1) + '.png',
                erasedEllipticalHard(image=image,
                                     axisShape=(random.randint(pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisShapeXLimits"][0], pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisShapeXLimits"][1]),
                                                random.randint(pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisShapeYLimits"][0], pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisShapeYLimits"][1])),
                                     refillColor=np.random.choice(a=pp.ImageNoiseParameters["ErasedEllipticalHard"]["refillColors"], size=1, p=pp.ImageNoiseParameters["ErasedEllipticalHard"]["refillColorProbabilities"])[0]))