import os, numpy as np

projectPath = os.path.join("D:".join(os.sep), "Codes", "Python", "Major Project")

generatedDirectoryPath = os.path.join(projectPath, "generated")
resrcDirectoryPath = os.path.join(projectPath, "resrc")
srcDirectoryPath = os.path.join(projectPath, "src")

corruptedDatasetDirectoryPath = os.path.join(generatedDirectoryPath, 'Corrupted')

inkDropDirectoryPath = os.path.join(resrcDirectoryPath, "Ink Drops")
untouchedDatasetDirectoryPath = os.path.join(resrcDirectoryPath, 'Untouched')

ImageNoiseParameters = dict()

ImageNoiseParameters["ErasedEllipticalHard"] = dict()
ImageNoiseParameters["ErasedEllipticalHard"]["axisShapeXLimits"] = (5, 10)
ImageNoiseParameters["ErasedEllipticalHard"]["axisShapeYLimits"] = (5, 10)
ImageNoiseParameters["ErasedEllipticalHard"]["refillColors"] = (0, 255)
ImageNoiseParameters["ErasedEllipticalHard"]["refillColorProbabilities"] = (0.25, 0.75)

ImageNoiseParameters["ErasedGaussian"] = dict()
ImageNoiseParameters["ErasedGaussian"]["shapeXLimits"] = (20, 25)
ImageNoiseParameters["ErasedGaussian"]["shapeYLimits"] = (20, 25)
ImageNoiseParameters["ErasedGaussian"]["sigmaXLimits"] = (5, 5)
ImageNoiseParameters["ErasedGaussian"]["shapeYLimits"] = (5, 5)
ImageNoiseParameters["ErasedGaussian"]["refillColors"] = (0, 255)
ImageNoiseParameters["ErasedGaussian"]["refillColorProbabilities"] = (0.25, 0.75)

