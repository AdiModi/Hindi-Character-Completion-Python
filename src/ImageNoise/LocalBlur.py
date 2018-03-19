import cv2, random, numpy as np

def localBlur(image, kSize=11, sigmaX=3, sigmaY=3):
    imageShape = image.shape

    center = (random.randint(0, imageShape[0] - 1), random.randint(0, imageShape[1] - 1))

    y, x = np.ogrid[-center[0]:imageShape[0] - center[0], -center[1]:imageShape[1] - center[1]]
    mask = x * x + y * y < int(kSize / 2) ** 2

    image[mask] = cv2.GaussianBlur(image, (kSize, kSize), sigmaX=sigmaX, sigmaY=sigmaY, borderType=cv2.BORDER_CONSTANT)[mask]
    return image

for i in range(0, 10):
    image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i + 1) + '.png', localBlur(image, sigmaY=2))