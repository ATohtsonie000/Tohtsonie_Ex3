import arcpy
from arcpy import env

arcpy.CreateFileGDB_management(r'C:\Users\atohtson\Desktop\Example_3_Python','classHW.gdb')

current_workspace = r'C:\Users\atohtson\Desktop\Example_3_Python\classHW.gdb'
geometry_type = "POLYGON"
spatial_reference = arcpy.SpatialReference(102100)
fetureClassNamesList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']
arcpy.env.workspace = current_workspace
arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):
	arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)
	print('Feature Class ' + in_fc_name + ' was sucessfull created.')

createFC = [createFeatureClass(fc) for fc in fetureClassNamesList]

print('All Done')

