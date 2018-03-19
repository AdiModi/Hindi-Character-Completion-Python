import cv2, numpy as np, random

WASHED_AWAY_NOISE_POSITION_RANDOM = 0
WASHED_AWAY_NOISE_POSITION_LEFT_TOP = 1
WASHED_AWAY_NOISE_POSITION_RIGHT_TOP = 2
WASHED_AWAY_NOISE_POSITION_RIGHT_BOTTOM = 3
WASHED_AWAY_NOISE_POSITION_LEFT_BOTTOM = 4

def saltAndPepperNoise(image, intensity=0.1):
    if intensity < 0 or intensity > 1:
        return image

    threshold = 10 - intensity
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            prob = random.random() * 10
            if prob < intensity:
                image[i][j] = 0
            elif prob > threshold:
                image[i][j] = 255
    return image

image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
imageShape = image.shape

noisyImageSaltAndPepper=saltAndPepperNoise(image=image, intensity=0.1)
cv2.imwrite('C:\\Users\\Aditya\\Desktop\\NOISY_TEST_SALT_AND_PEPPER.png', noisyImageSaltAndPepper)