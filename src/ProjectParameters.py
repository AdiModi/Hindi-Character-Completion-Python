import os, numpy as np

imageDimension = 32

projectPath = os.path.join("D:".join(os.sep), "Codes", "Python", "Hindi Character Completion")

generatedDirectoryPath = os.path.join(projectPath, "generated")
resrcDirectoryPath = os.path.join(projectPath, "resrc")
srcDirectoryPath = os.path.join(projectPath, "src")

corruptedDatasetDirectoryPath = os.path.join(generatedDirectoryPath, 'Corrupted')
serialImagesDatasetFilePath = os.path.join(generatedDirectoryPath, 'Serial Images Dataset.mat')
nonSerialImagesDatasetFilePath = os.path.join(generatedDirectoryPath, 'Non Serial Images Dataset.mat')

inkDropDirectoryPath = os.path.join(resrcDirectoryPath, "Ink Drops")
untouchedDatasetDirectoryPath = os.path.join(resrcDirectoryPath, 'Untouched')

ImageCorruptionParameters = dict()

ImageCorruptionParameters["ErasedEllipticalHard"] = dict()
ImageCorruptionParameters["ErasedEllipticalHard"]["axisLengthXLimits"] = (5, 10)
ImageCorruptionParameters["ErasedEllipticalHard"]["axisLengthYLimits"] = (5, 10)
ImageCorruptionParameters["ErasedEllipticalHard"]["refillColors"] = (0, 255)
ImageCorruptionParameters["ErasedEllipticalHard"]["refillColorProbabilities"] = (0.75, 0.25)

ImageCorruptionParameters["ErasedRectangleHard"] = dict()
ImageCorruptionParameters["ErasedRectangleHard"]["lengthXLimits"] = (10, 25)
ImageCorruptionParameters["ErasedRectangleHard"]["lengthYLimits"] = (10, 25)
ImageCorruptionParameters["ErasedRectangleHard"]["refillColors"] = (0, 255)
ImageCorruptionParameters["ErasedRectangleHard"]["refillColorProbabilities"] = (0.75, 0.25)

ImageCorruptionParameters["InkDrop"] = dict()
ImageCorruptionParameters["InkDrop"]["filterSize"] = (32, 32)

ImageCorruptionParameters["SaltAndPepper"] = dict()
ImageCorruptionParameters["SaltAndPepper"]["probability"] = 0.1

ImageCorruptionParameters["LocalBlur"] = dict()
ImageCorruptionParameters["LocalBlur"]["kSize"] = (11, 11)
ImageCorruptionParameters["LocalBlur"]["sigma"] = (2, 2)

ImageCorruptionParameters["ErasedGaussian"] = dict()
ImageCorruptionParameters["ErasedGaussian"]["shapeXLimits"] = (25, 30)
ImageCorruptionParameters["ErasedGaussian"]["shapeYLimits"] = (25, 30)
ImageCorruptionParameters["ErasedGaussian"]["sigmaXLimits"] = (7, 7)
ImageCorruptionParameters["ErasedGaussian"]["sigmaYLimits"] = (7, 7)
ImageCorruptionParameters["ErasedGaussian"]["refillColor"] = 0