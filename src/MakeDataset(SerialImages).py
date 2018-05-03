import ProjectParameters as pp
import scipy.io as sio
import numpy as np, time

start_time = time.time()

nonSerialImagesDatasetFilePath = sio.loadmat(pp.nonSerialImagesDatasetFilePath)

trainInputImages = nonSerialImagesDatasetFilePath['trainInputImages']
trainOutputImages = nonSerialImagesDatasetFilePath['trainOutputImages']
testInputImages = nonSerialImagesDatasetFilePath['testInputImages']
testOutputImages = nonSerialImagesDatasetFilePath['testOutputImages']

trainInputImages = trainInputImages.reshape((len(trainInputImages), 1, pp.imageDimension * pp.imageDimension))
trainInputImages = np.squeeze(trainInputImages, axis = 1)
trainOutputImages = trainOutputImages.reshape((len(trainOutputImages), 1, pp.imageDimension * pp.imageDimension))
trainOutputImages = np.squeeze(trainOutputImages, axis = 1)
testInputImages = testInputImages.reshape((len(testInputImages), 1, pp.imageDimension * pp.imageDimension))
testInputImages = np.squeeze(testInputImages, axis = 1)
testOutputImages = testOutputImages.reshape((len(testOutputImages), 1, pp.imageDimension * pp.imageDimension))
testOutputImages = np.squeeze(testOutputImages, axis = 1)

sio.savemat(pp.serialImagesDatasetFilePath, {
    "trainInputImages": trainInputImages,
    "trainOutputImages": trainOutputImages,
    "testInputImages": testInputImages,
    "testOutputImages": testOutputImages
})

print("Complete Execution Time to generate Non Serial Images Dataset in .mat file is %s seconds " %(time.time() - start_time))