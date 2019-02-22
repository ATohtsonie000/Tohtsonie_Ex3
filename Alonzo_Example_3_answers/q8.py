import arcpy
arcpy.env.workspace = r"C:\Users\atohtson\Desktop\Exercise3\Example_3_Python\Exercise 3.gdb"
arcpy.GetCount_management("CallsforService")

print len(arcpy.ListFeatureClasses())