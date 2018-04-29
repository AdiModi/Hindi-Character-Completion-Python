import numpy as np, glob, os, cv2
import keras.layers as layers
from keras.layers import Conv2D, UpSampling2D
from keras.models import Model

inputImagesDirectoryPath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'generated', 'Corrupted', 'test')
outputImagesDirectoryPath = os.path.join('D:\\', 'Codes', 'Python', 'Hindi Character Completion', 'resrc', 'Untouched', 'test')

noOfLabels = 46
imagesPerLabel = 300
imageDimension = 32

corruptImageFileNamePrefixes = ['EEH_', 'EG_', 'ERH_', 'ID_', 'LB_', 'S&P_']

inputImages = np.ndarray(shape=(imagesPerLabel*len(corruptImageFileNamePrefixes)*noOfLabels, imageDimension, imageDimension, 1))
outputImages = np.ndarray(shape=(imagesPerLabel*len(corruptImageFileNamePrefixes)*noOfLabels, imageDimension, imageDimension, 1))

def makeDataset(inputImagesDirectoryPath='', outputImagesDirectoryPath=''):
    imagePaths = glob.glob(os.path.join(outputImagesDirectoryPath, '*.png'))

    for imagePath in imagePaths:
        imageName = imagePath[imagePath.rindex(os.sep) + 1:]
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        for i in range(len(corruptImageFileNamePrefixes)):
            np.append(outputImages, image)

        for i in range(len(corruptImageFileNamePrefixes)):
            image = cv2.imread(os.path.join(inputImagesDirectoryPath, corruptImageFileNamePrefixes[i] + str(imageName)), cv2.IMREAD_GRAYSCALE)
            np.append(inputImages, image)

    for item in os.listdir(outputImagesDirectoryPath):
        if os.path.isdir(os.path.join(outputImagesDirectoryPath, item)):
            makeDataset(os.path.join(inputImagesDirectoryPath, item), os.path.join(outputImagesDirectoryPath, item))

makeDataset(inputImagesDirectoryPath, outputImagesDirectoryPath)

inputLayer = layers.Input(shape=(imageDimension, imageDimension, 1), dtype=np.float32)
layer = layers.Conv2D(32, (4, 4), activation='relu', padding='same')(inputLayer)
layer = layers.MaxPooling2D((2, 2), padding='same')(layer)
layer = layers.Conv2D(32, (4, 4), activation='relu', padding='same')(layer)
encoded = layers.MaxPooling2D((2, 2), padding='same')(layer)

layer = Conv2D(32, (3, 3), activation='relu', padding='same')(encoded)
layer = UpSampling2D((2, 2))(layer)
layer = Conv2D(32, (3, 3), activation='relu', padding='same')(layer)
layer = UpSampling2D((2, 2))(layer)
decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(layer)

autoencoder = Model(inputLayer, decoded)
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

autoencoder.fit(inputImages, outputImages,
                epochs=100,
                batch_size=128,
                shuffle=True,
                validation_data=(inputImages, outputImages))