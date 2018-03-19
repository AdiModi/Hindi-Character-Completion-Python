import cv2, numpy as np, random

def erasedRectangleHard(image, shape=(1, 1), refillColor=0):
    if shape[0] == 0 or shape[1] == 0:
        return image

    imageShape = image.shape

    startRowIndex = random.randint(0, imageShape[0] - shape[0])
    endRowIndex = startRowIndex + shape[0] - 1
    startColumnIndex = random.randint(0, imageShape[1] - shape[1])
    endColumnIndex = startColumnIndex + shape[1] - 1

    blendMatrix = np.zeros((imageShape[0], imageShape[1]))
    blendMatrix[startRowIndex: endRowIndex + 1, startColumnIndex: endColumnIndex + 1] = 1

    M = cv2.getRotationMatrix2D((int(imageShape[1]/2), int(imageShape[0]/2)), random.randint(0, 360), random.uniform(0.7, 1))
    blendMatrix = cv2.warpAffine(blendMatrix, M, (imageShape[1], imageShape[1]))

    image=np.multiply(image, 1 - blendMatrix) + np.multiply(refillColor, blendMatrix)
    return image

for i in range(0, 20):
    image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i+1) + '.png', erasedRectangleHard(image=image, shape=(random.randint(10, 20), random.randint(10, 20)), refillColor=0))