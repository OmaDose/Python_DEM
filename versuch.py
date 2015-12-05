#!/bin/python
# -*- coding: iso-8859-15 -*-
#Author: Johanna Schwehn 2015
#Assignment 2 
#Generate a 3D Point Cloud of the Cell Centers of a DEM
#python rast2cloud.py dsm.tif output_ascii.xyz min_elevation max_elevation
###########################################


#required modules
import sys
from numpy import *
from osgeo import gdal

#enable error-reports by rising exceptions fpr GDAL
gdal.UseExceptions()

#arguments provided as user input
try:
	infile = sys.argv[1] #dsm.tif
	outfile = sys.argv[2] #output_ascii.xyz
	#min_elevation  = sys.argv[3] #min_elevation
	#max_elevation = sys.argv[4] #max_elevation 
except:
	print "rast2cloud.py dsm.tif output_ascii.xyz min_elevation max_elevation"
	sys.exit(1)
	
#Open existing dataset
src_ds = gdal.Open( infile )

#Open output format driver, see gdal_translate --formats for list
format = "XYZ"
driver = gdal.GetDriverByName( format )

#Output to new format
dst_ds = driver.CreateCopy( outfile, src_ds, 0 )


#Properly close the datasets to flush to disk
dst_ds = None
src_ds = None