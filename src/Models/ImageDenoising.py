import numpy as np, cv2, time
import ProjectParameters as pp
import scipy.io as sio
import keras.layers as layers
from keras.layers import Conv2D, UpSampling2D
from keras.models import Model

start_time = time.time()

imageDimension = 32

nonSerialImagesDatasetFilePath = sio.loadmat(pp.nonSerialImagesDatasetFilePath)

trainInputImages = np.expand_dims(nonSerialImagesDatasetFilePath['trainInputImages'], axis=3)
trainOutputImages = np.expand_dims(nonSerialImagesDatasetFilePath['trainOutputImages'], axis=3)
testInputImages = np.expand_dims(nonSerialImagesDatasetFilePath['testInputImages'], axis=3)
testOutputImages = np.expand_dims(nonSerialImagesDatasetFilePath['testOutputImages'], axis=3)

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

print(autoencoder.summary())

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

autoencoder.fit(trainInputImages, trainOutputImages,
                epochs=10,
                shuffle=True,
                validation_data=(trainInputImages, trainOutputImages))

cv2.imshow("Image", testInputImages[0])
cv2.waitKey(0)

image = autoencoder.predict(testInputImages[0], verbose=0)
cv2.imshow("Image", image)
cv2.waitKey(0)

print("Complete Execution Time to train the Dataset is %s seconds " %(time.time() - start_time))