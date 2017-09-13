# Author:  
# Date:
# Purpose:  To List all Feature Classes in GDB


# Import ArcPy
import arcpy
 

# Set the workspace
arcpy.env.workspace = r"C:\Users\Aaron\Desktop\School\JHU Master's Program\2017\Programming_in_GIS\Module2\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase 
featureClasses= arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for fc in featureClasses:
    print(fc)

# Print "Complete"
print "Complete"
