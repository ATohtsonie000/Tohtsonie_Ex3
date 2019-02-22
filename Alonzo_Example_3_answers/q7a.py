import arcpy
from arcpy import env

arcpy.env.workspace = r"C:\Users\atohtson\Desktop\Exercise_3_Working_18FEB19\Exercise3\Example_3_Python\Exercise_three.gdb"

arcpy.env.overwriteOutput = True

inFeatures = r"C:\Users\atohtson\Desktop\Exercise_3_Working_18FEB19\Exercise3\Example_3_Python\Exercise_three.gdb\CallsforService"

outLocation = "FeaturetoFeature"

arcpy.MakeFeatureLayer_management (inFeatures,'CallsforService_lyr') 

arcpy.SelectLayerByAttribute_management('CallsforService_lyr','NEW_SELECTION',"CFSType = 'Alarm Call'")

arcpy.CopyFeatures_management('CallsforService_lyr',r'C:\Users\atohtson\Desktop\Exercise_3_Working_18FEB19\Exercise3\Example_3_Python\Exercise_three.gdb\New_Selection')
print ('all done') 
