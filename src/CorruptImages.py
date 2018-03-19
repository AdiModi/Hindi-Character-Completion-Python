import glob, os, cv2, tqdm, random, numpy as np
from src.ImageNoise import ErasedGaussian, ErasedEllipticalHard, ErasedRectangleHard, InkDrop, LocalBlur, SaltAndPepper
from src import ProjectParameters as pp

untouchedDatasetDirectoryPath = ''
# D:\Codes\Python\Major Project\resrc\Untouched\test\0
corruptedDatasetDirectoryPath = ''
# D:\Codes\Python\Major Project\resrc\Corrupted\test\0

def corruptImagesFromDirectoryRecursively(sourceDirectoryPath='',
                                          destinationDirectoryPath=''):
    imagePaths = glob.glob(os.path.join(sourceDirectoryPath, '*.png'))
    totalImages = len(imagePaths)

    print('Corrupting images from: \'' + sourceDirectoryPath + '\'\nAnd Saving it to: \'' + destinationDirectoryPath + '\'')
    progressBar = tqdm.tqdm(total=totalImages, dynamic_ncols=False, unit=' Images', initial=0, ncols=100)

    for imagePath in imagePaths:
        imageName = imagePath[imagePath.rindex(os.sep) + 1:]
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        # Performing Erased Elliptical Hard
        cv2.imwrite(os.path.join(destinationDirectoryPath, 'EEH_' + imageName),
                    ErasedEllipticalHard.erasedEllipticalHard(image=image.copy(),
                                                              axisLength=(random.randint(pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthXLimits"][0], pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthXLimits"][1]),
                                                                          random.randint(pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthYLimits"][0], pp.ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthYLimits"][1])),
                                                              refillColor=np.random.choice(a=pp.ImageNoiseParameters["ErasedEllipticalHard"]["refillColors"],
                                                                                           size=1,
                                                                                           p=pp.ImageNoiseParameters["ErasedEllipticalHard"]["refillColorProbabilities"])[0]))

        # Performing Erased Gaussian
        cv2.imwrite(os.path.join(destinationDirectoryPath, 'EG_' + imageName),
                    ErasedGaussian.erasedGaussian(image=image.copy(),
                                                  erasedShape=(random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["shapeXLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["shapeXLimits"][1]),
                                                               random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["shapeYLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["shapeYLimits"][1])),
                                                  sigma=(random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["sigmaXLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["sigmaXLimits"][1]),
                                                         random.randint(pp.ImageNoiseParameters["ErasedGaussian"]["sigmaYLimits"][0], pp.ImageNoiseParameters["ErasedGaussian"]["sigmaYLimits"][1])),
                                                  refillColor=pp.ImageNoiseParameters["ErasedGaussian"]["refillColor"]))

        # Performing Erased Rectangle Hard
        cv2.imwrite(os.path.join(destinationDirectoryPath, 'ERH_' + imageName),
                    ErasedRectangleHard.erasedRectangleHard(image=image.copy(),
                                                            shape=(random.randint(pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthXLimits"][0], pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthXLimits"][1]),
                                                                   random.randint(pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthYLimits"][0], pp.ImageNoiseParameters["ErasedRectangleHard"]["lengthYLimits"][1])),
                                                            refillColor=np.random.choice(a=pp.ImageNoiseParameters["ErasedRectangleHard"]["refillColors"],
                                                                                         size=1,
                                                                                         p=pp.ImageNoiseParameters["ErasedRectangleHard"]["refillColorProbabilities"])[0]))

        # Performing Ink Drop
        cv2.imwrite(os.path.join(destinationDirectoryPath, 'ID_' + imageName),
                    InkDrop.inkDrop(image=image.copy()))

        # Performing Local Blur
        cv2.imwrite(os.path.join(destinationDirectoryPath, 'LB_' + imageName),
                    LocalBlur.localBlur(image=image.copy(),
                                        kSize=pp.ImageNoiseParameters["LocalBlur"]["kSize"],
                                        sigma=pp.ImageNoiseParameters["LocalBlur"]["sigma"]))

        # Performing Salt And Pepper
        cv2.imwrite(os.path.join(destinationDirectoryPath, 'S&P_' + imageName),
                    SaltAndPepper.saltAndPepper(image=image,
                                                probability=pp.ImageNoiseParameters["SaltAndPepper"]["probability"]))

        progressBar.update(1)

    progressBar.close()

    for item in os.listdir(sourceDirectoryPath):
        if os.path.isdir(os.path.join(sourceDirectoryPath, item)):
            os.mkdir(os.path.join(destinationDirectoryPath, item))
            corruptImagesFromDirectoryRecursively(os.path.join(sourceDirectoryPath, item),
                                                  os.path.join(destinationDirectoryPath, item))

# untouchedDatasetDirectoryPath = os.path.join('D:'.join(os.sep), 'Codes', 'Python', 'Major Project', 'resrc', 'Untouched')
# untouchedDatasetDirectoryPath = input('Please enter the root directory path: ')
# while True:
#     if not os.path.isdir(untouchedDatasetDirectoryPath):
#         print(untouchedDatasetDirectoryPath)
#         print('Directory path does not exist!\n')
#         untouchedDatasetDirectoryPath = input('Please enter a valid directory path: ')
#     else:
#         break
#
# corruptedDatasetDirectoryPath = os.path.join('D:'.join(os.sep), 'Codes', 'Python', 'Major Project', 'resrc', 'Corrupted')
#
# corruptedDatasetDirectoryPath = input('Please enter the root directory path: ')
# if not os.path.isdir(corruptedDatasetDirectoryPath):
#     os.mkdir(corruptedDatasetDirectoryPath)

# corruptImagesFromDirectoryRecursively(sourceDirectoryPath=untouchedDatasetDirectoryPath,
#                                       destinationDirectoryPath=corruptedDatasetDirectoryPath)

corruptImagesFromDirectoryRecursively(sourceDirectoryPath='C:\\Users\\Aditya\\Desktop\\Test',
                                      destinationDirectoryPath='C:\\Users\\Aditya\\Desktop\\Corrupted')