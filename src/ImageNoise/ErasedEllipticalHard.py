import cv2, numpy as np, random

def erasedEllipticalHard(image, axisLength=(1, 1), refillColor=0):

    # Taking Image Size
    imageShape = image.shape

    #Calculating the center of the ellipse
    center = (random.randint(0, imageShape[0] - 1), random.randint(0, imageShape[1] - 1))

    # Creating the blend matrix
    blendMatrix = np.zeros((imageShape[0], imageShape[1]))

    # Creating boolean mask for pixels
    y, x = np.ogrid[-center[0]:imageShape[0] - center[0], -center[1]:imageShape[1] - center[1]]
    booleanMask = ((x ** 2) / (axisLength[1] ** 2)) + ((y ** 2) / (axisLength[0] ** 2)) < 1
    blendMatrix[booleanMask] = 1

    # Rotating the blend matrix
    M = cv2.getRotationMatrix2D((center[0], center[1]), random.randint(0, 360), 1)
    blendMatrix = cv2.warpAffine(blendMatrix, M, (imageShape[1], imageShape[0]))

    # Applying it to the image
    image = np.multiply(image, 1 - blendMatrix) + np.multiply(refillColor, blendMatrix)
    return image

# for i in range(0, 20):
#     image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
#     cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i+1) + '.png',
#                 erasedEllipticalHard(image=image,
#                                      axisLength=(random.randint(pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthXLimits"][0], pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthXLimits"][1]),
#                                                  random.randint(pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthYLimits"][0], pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthYLimits"][1])),
#                                      refillColor=np.random.choice(a=pp.ImageNoiseParameters["ErasedEllipticalHard"]["refillColors"], size=1, p=pp.ImageNoiseParameters["ErasedEllipticalHard"]["refillColorProbabilities"])[0]))