import cv2, random, numpy as np
from src import ProjectParameters as pp

def localBlur(image, kSize=(11, 11), sigma=(3, 3)):

    # Taking Image Size
    imageShape = image.shape

    # Calculating the center of the ellipse
    center = (random.randint(0, imageShape[0] - 1), random.randint(0, imageShape[1] - 1))

    # Creating boolean mask for pixels
    y, x = np.ogrid[-center[0]:imageShape[0] - center[0], -center[1]:imageShape[1] - center[1]]
    booleanMask = ((x ** 2) / (kSize[1] ** 2)) + ((y ** 2) / (kSize[0] ** 2)) < 1

    # Applying it to the image
    image[booleanMask] = cv2.GaussianBlur(image, (kSize[0], kSize[1]), sigmaX=sigma[0], sigmaY=sigma[1], borderType=cv2.BORDER_CONSTANT)[booleanMask]
    return image

# for i in range(0, 20):
#     image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
#     cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i + 1) + '.png',
#                 localBlur(image=image,
#                           kSize=pp.ImageNoiseParameters["LocalBlur"]["kSize"],
#                           sigma=pp.ImageNoiseParameters["LocalBlur"]["sigma"]))