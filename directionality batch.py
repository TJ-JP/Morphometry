import os, sys
from os import path
from fiji.analyze.directionality import Directionality_
from ij import WindowManager, ImagePlus, IJ
from ij.io import FileSaver

inputdir = "C:/Users/DELL/Desktop/Re2/Mike/epoch1000/Directionality/frac/"
output = "C:\Users\DELL\Desktop\Re2\Mike\original_patches256x256\Directionality"

# Instantiate plugin
dir = Directionality_()

images = os.listdir(inputdir)
for image in images:
	imp = path.join(inputdir, image) 
	imp = IJ.open(imp) 
	filename = os.path.basename(image)
	filename = filename.split(".")[0]
	IJ.run(imp,"Make Binary","")
	IJ.run(imp, "Despeckle","")
	dir.setImagePlus(WindowManager.getCurrentImage())
	# Set fields and settings	
	dir.setMethod(Directionality_.AnalysisMethod.LOCAL_GRADIENT_ORIENTATION)
	#dir.setMethod(Directionality_.AnalysisMethod.FOURIER_COMPONENTS)
	dir.setBinNumber(90)
	dir.setBinStart(-90)
	dir.setBuildOrientationMapFlag(True)	
	# Do calculation
	dir.computeHistograms()
	dir.fitHistograms()
	# Display results table
	table = dir.displayResultsTable()
	table.show("Directionality histograms")
	IJ.saveAs("displayResultsTable", "C:/Users/DELL/Desktop/Re2/Mike/epoch1000/Directionality/Directionality" + filename + ".xls")
	IJ.run("Close")	
	# Display orientation map
	stack = dir.getOrientationMap()
	img = ImagePlus("Orientation map", stack).show()
	IJ.saveAs(img, "JPG", "C:/Users/DELL/Desktop/Re2/Mike/epoch1000/Directionality/Directionality" + filename + ".jpg")
	IJ.run("Close")
	



