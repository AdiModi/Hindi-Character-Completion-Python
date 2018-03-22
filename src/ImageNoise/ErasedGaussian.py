import cv2, random, math, numpy as np

def erasedGaussian(image, erasedShape=(1, 1), sigma=(1, 1), refillColor=0):

    if erasedShape[0] == 0 or erasedShape[1] == 0:
        return image

    # Taking Image Size
    imageShape = image.shape

    x = random.randint(0, imageShape[0])
    rowIndices = (erasedShape[0] + x - math.floor(erasedShape[0] / 2), erasedShape[0] + x + math.ceil(erasedShape[0] / 2) - 1)
    y = random.randint(0, imageShape[1])
    columnIndices = (erasedShape[1] + y - math.floor(erasedShape[1] / 2), erasedShape[1] + y + math.ceil(erasedShape[1] / 2) - 1)

    kernel = cv2.getGaussianKernel(erasedShape[0], sigma[0]) * cv2.getGaussianKernel(erasedShape[1], sigma[1]).T
    kernel = cv2.normalize(kernel, kernel, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    for i in range(rowIndices[0], rowIndices[1] + 1):
        for j in range(columnIndices[0], columnIndices[1] + 1):
            if i >= erasedShape[0] and j >= erasedShape[1] and i < imageShape[0]+erasedShape[0] and j < imageShape[1]+erasedShape[1]:
                alpha = kernel[i - rowIndices[0], j - columnIndices[0]]
                image[i - erasedShape[0], j - erasedShape[1]] = alpha * refillColor + (1 - alpha) * image[i - erasedShape[0], j - erasedShape[1]]

    return image

# for i in range(0, 20):
#     image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
#     cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i+1) + '.png',
#                 erasedGaussian(image=image,
#                                erasedShape=(random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["shapeXLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["shapeXLimits"][1]),
#                                             random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["shapeYLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["shapeYLimits"][1])),
#                                sigma=(random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["sigmaXLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["sigmaXLimits"][1]),
#                                       random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["sigmaYLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["sigmaYLimits"][1])),
#                                refillColor=pp.ImageNoiseParameters["ErasedGaussian"]["refillColor"]))