import cv2, numpy as np

def saltAndPepper(image, probability=0.1):
    if probability < 0 or probability > 1:
        return image

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = np.random.choice(a=(image[i][j], 0, 255), size=1, p=(1-probability, probability/2, probability/2))
    return image

# for i in range(0, 20):
#     image = cv2.imread('C:\\Users\\Aditya\\Desktop\\TEST_IMG.png', cv2.IMREAD_GRAYSCALE)
#     cv2.imwrite('C:\\Users\\Aditya\\Desktop\\Noisy_' + str(i+1) + '.png',
#                 saltAndPepperNoise(image=image,
#                                    probability=pp.ImageNoiseParameters["SaltAndPepper"]["probability"]))