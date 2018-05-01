import numpy as np, glob, os, cv2, scipy, tqdm

trainInputImagesDirectoryPath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'generated', 'Corrupted', 'train')
trainOutputImagesDirectoryPath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'resrc', 'Untouched', 'train')
testInputImagesDirectoryPath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'generated', 'Corrupted', 'test')
testOutputImagesDirectoryPath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'resrc', 'Untouched', 'test')

trainInputImagesDatasetFilePath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'generated', 'inputImages(Train).mat')
trainOutputImagesDatasetFilePath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'generated', 'outputImages(Train).mat')
testInputImagesDatasetFilePath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'generated', 'inputImages(Test).mat')
testOutputImagesDatasetFilePath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'generated', 'outputImages(Test).mat')

noOfLabels = 46
trainImagesPerLabel = 1700
testImagesPerLabel = 300
imageDimension = 32

corruptImageFileNamePrefixes = ['EEH_', 'EG_', 'ERH_', 'ID_', 'LB_', 'S&P_']

trainInputImages = np.ndarray(shape=(trainImagesPerLabel*len(corruptImageFileNamePrefixes)*noOfLabels, imageDimension, imageDimension, 1))
trainOutputImages = np.ndarray(shape=(trainImagesPerLabel*len(corruptImageFileNamePrefixes)*noOfLabels, imageDimension, imageDimension, 1))
testInputImages = np.ndarray(shape=(testImagesPerLabel*len(corruptImageFileNamePrefixes)*noOfLabels, imageDimension, imageDimension, 1))
testOutputImages = np.ndarray(shape=(testImagesPerLabel*len(corruptImageFileNamePrefixes)*noOfLabels, imageDimension, imageDimension, 1))

def recursivelyGatherImages(inputImagesDirectoryPath='', outputImagesDirectoryPath='', inputImages = np.ndarray(shape=(0, imageDimension, imageDimension, 1)), outputImages = np.ndarray(shape=(0, imageDimension, imageDimension, 1))):

    imagePaths = glob.glob(os.path.join(outputImagesDirectoryPath, '*.png'))
    progressBar = tqdm.tqdm(total=len(imagePaths), dynamic_ncols=False, unit=' Images', initial=0, ncols=100)

    for imagePath in imagePaths:
        imageName = imagePath[imagePath.rindex(os.sep) + 1:]
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        for i in range(len(corruptImageFileNamePrefixes)):
            np.append(outputImages, image)

        for i in range(len(corruptImageFileNamePrefixes)):
            image = cv2.imread(os.path.join(inputImagesDirectoryPath, corruptImageFileNamePrefixes[i] + str(imageName)), cv2.IMREAD_GRAYSCALE)
            np.append(inputImages, image)

        progressBar.update(1)

    progressBar.close()

    for item in os.listdir(outputImagesDirectoryPath):
        if os.path.isdir(os.path.join(outputImagesDirectoryPath, item)):
            recursivelyGatherImages(os.path.join(inputImagesDirectoryPath, item), os.path.join(outputImagesDirectoryPath, item))

    return inputImages, outputImages

# print("Generating and Saving Train Dataset...")
# trainInputImages, trainOutputImages = recursivelyGatherImages(trainInputImagesDirectoryPath, testOutputImagesDirectoryPath, inputImages=trainInputImages, outputImages=trainOutputImages)
# scipy.io.savemat(trainInputImagesDatasetFilePath, trainInputImages)
# scipy.io.savemat(trainOutputImagesDatasetFilePath, trainOutputImages)

print("Generating and Saving Test Dataset...")
testInputImages, testOutputImages = recursivelyGatherImages(trainInputImagesDirectoryPath, testOutputImagesDirectoryPath, inputImages=testInputImages, outputImages=testOutputImages)
scipy.io.savemat(testInputImagesDatasetFilePath, testInputImages)
scipy.io.savemat(testOutputImagesDatasetFilePath, testOutputImages)