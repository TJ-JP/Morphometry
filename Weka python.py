import os
from trainableSegmentation import WekaSegmentation, Weka_Segmentation
from ij import IJ, ImagePlus
from ij.plugin import LutLoader
import time
 
def run():
	srcDir = r'G:\UK\patches\Copy\Combined_copy'
	dstDir = r'G:\UK\patches\Copy\cc'
	for root, directories, filenames in os.walk(srcDir):
		filenames.sort();
		for filename in filenames:
      		# Check for file extension
			if not filename.endswith('.jpg'):
        			continue
			process(srcDir, dstDir, root, filename)
 
def process(srcDir, dstDir, currentDir, fileName):
	print "Processing:"

	# Opening the image
	print "Open image file", fileName
	image = IJ.openImage(os.path.join(srcDir, fileName))

	weka = WekaSegmentation()
	weka.setTrainingImage(image)
	time.sleep(1000)

	# loads manually trained classifier
	weka.loadClassifier(r'G:\UK\patches\Copy\classifier.model')
	time.sleep(1000)
	# apply classifier and get results
	segmented_image = weka.applyClassifier(image, 0, False)
	time.sleep(1000)
	# assign same LUT as in GUI. Within WEKA GUI, right-click on classified image and use Command Finder to save the "LUT" within Fiji.app\luts
	lut = LutLoader.openLut(r'G:\UK\patches\Copy\lut\Trainable Weka Segmentation v3.3.2.lut')
	segmented_image.getProcessor().setLut(lut)

	# Saving the image as a .tif file
	saveDir = dstDir
	if not os.path.exists(saveDir):
		os.makedirs(saveDir)
	print "Saving to", saveDir
	IJ.saveAs(segmented_image, "png", os.path.join(saveDir, fileName))
	image.close()

run()