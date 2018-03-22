import os, numpy as np

projectPath = os.path.join("D:".join(os.sep), "Codes", "Python", "Hindi Character Completion")

generatedDirectoryPath = os.path.join(projectPath, "generated")
resrcDirectoryPath = os.path.join(projectPath, "resrc")
srcDirectoryPath = os.path.join(projectPath, "src")

corruptedDatasetDirectoryPath = os.path.join(generatedDirectoryPath, 'Corrupted')

inkDropDirectoryPath = os.path.join(resrcDirectoryPath, "Ink Drops")
untouchedDatasetDirectoryPath = os.path.join(resrcDirectoryPath, 'Untouched')

ImageNoiseParameters = dict()

ImageNoiseParameters["ErasedEllipticalHard"] = dict()
ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthXLimits"] = (5, 10)
ImageNoiseParameters["ErasedEllipticalHard"]["axisLengthYLimits"] = (5, 10)
ImageNoiseParameters["ErasedEllipticalHard"]["refillColors"] = (0, 255)
ImageNoiseParameters["ErasedEllipticalHard"]["refillColorProbabilities"] = (0.75, 0.25)

ImageNoiseParameters["ErasedRectangleHard"] = dict()
ImageNoiseParameters["ErasedRectangleHard"]["lengthXLimits"] = (10, 25)
ImageNoiseParameters["ErasedRectangleHard"]["lengthYLimits"] = (10, 25)
ImageNoiseParameters["ErasedRectangleHard"]["refillColors"] = (0, 255)
ImageNoiseParameters["ErasedRectangleHard"]["refillColorProbabilities"] = (0.75, 0.25)

ImageNoiseParameters["InkDrop"] = dict()
ImageNoiseParameters["InkDrop"]["filterSize"] = (32, 32)

ImageNoiseParameters["SaltAndPepper"] = dict()
ImageNoiseParameters["SaltAndPepper"]["probability"] = 0.1

ImageNoiseParameters["LocalBlur"] = dict()
ImageNoiseParameters["LocalBlur"]["kSize"] = (11, 11)
ImageNoiseParameters["LocalBlur"]["sigma"] = (2, 2)

ImageNoiseParameters["ErasedGaussian"] = dict()
ImageNoiseParameters["ErasedGaussian"]["shapeXLimits"] = (25, 30)
ImageNoiseParameters["ErasedGaussian"]["shapeYLimits"] = (25, 30)
ImageNoiseParameters["ErasedGaussian"]["sigmaXLimits"] = (7, 7)
ImageNoiseParameters["ErasedGaussian"]["sigmaYLimits"] = (7, 7)
ImageNoiseParameters["ErasedGaussian"]["refillColor"] = 0