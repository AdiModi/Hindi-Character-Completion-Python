import numpy as np, glob, os, cv2
import scipy.io as sio
import tqdm, time
import ProjectParameters as pp

start_time = time.time()

trainInputImagesDirectoryPath = os.path.join(pp.corruptedDatasetDirectoryPath, 'train')
trainOutputImagesDirectoryPath = os.path.join(pp.untouchedDatasetDirectoryPath, 'train')
testInputImagesDirectoryPath = os.path.join(pp.corruptedDatasetDirectoryPath, 'test')
testOutputImagesDirectoryPath = os.path.join(pp.untouchedDatasetDirectoryPath, 'test')

corruptImageFileNamePrefixes = ['EEH_', 'EG_', 'ERH_', 'ID_', 'LB_', 'S&P_']

def recursivelyGatherImages(inputImagesDirectoryPath='', outputImagesDirectoryPath=''):

    print("Currently Processing:")
    print("\tInput Directory:", inputImagesDirectoryPath, sep=' ')
    print("\tOutput Directory:", outputImagesDirectoryPath, sep=' ')

    imagePaths = glob.glob(os.path.join(outputImagesDirectoryPath, '*.png'))

    progressBar = tqdm.tqdm(total=len(imagePaths), dynamic_ncols=True, unit=' Images', initial=0, ncols=80)

    inputImages = np.ndarray(shape=(0, pp.imageDimension, pp.imageDimension), dtype=np.uint8)
    outputImages = np.ndarray(shape=(0, pp.imageDimension, pp.imageDimension), dtype=np.uint8)

    for imagePath in imagePaths:
        imageName = imagePath[imagePath.rindex(os.sep) + 1:]
        # Reading Output Image Once and Adding it len(corruptImageFileNamePrefixes) times
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        for i in range(len(corruptImageFileNamePrefixes)):
            outputImages = np.concatenate((outputImages, np.expand_dims(image, axis=0)), axis=0)

        #Respectively readin Input Images and adding it accordingly
        for i in range(len(corruptImageFileNamePrefixes)):
            image = cv2.imread(os.path.join(inputImagesDirectoryPath, corruptImageFileNamePrefixes[i] + str(imageName)), cv2.IMREAD_GRAYSCALE)
            inputImages = np.concatenate((inputImages, np.expand_dims(image, axis=0)), axis=0)

        progressBar.update(1)

    progressBar.close()

    for item in os.listdir(outputImagesDirectoryPath):
        if os.path.isdir(os.path.join(outputImagesDirectoryPath, item)):
            tempInputImages, tempOutputImages = recursivelyGatherImages(os.path.join(inputImagesDirectoryPath, item), os.path.join(outputImagesDirectoryPath, item))
            inputImages = np.concatenate((inputImages, tempInputImages), axis=0)
            outputImages = np.concatenate((outputImages, tempOutputImages), axis=0)

    return inputImages, outputImages

print("Gathering Train Dataset: ")
trainInputImages, trainOutputImages = recursivelyGatherImages(trainInputImagesDirectoryPath, trainOutputImagesDirectoryPath)
print("Gathering Test Dataset: ")
testInputImages, testOutputImages = recursivelyGatherImages(testInputImagesDirectoryPath, testOutputImagesDirectoryPath)
sio.savemat(pp.nonSerialImagesDatasetFilePath, {
    "trainInputImages": trainInputImages,
    "trainOutputImages": trainOutputImages,
    "testInputImages": testInputImages,
    "testOutputImages": testOutputImages
})

print("Complete Execution Time to generate Non Serial Images Dataset in .mat file is %s seconds " %(time.time() - start_time))