import arcpy
from arcpy import env
env.overwriteOutput=True

target_features = r"C:\Users\atohtson\Desktop\Exercise_3_Working_20FEB19\Exercise3\Example_3_Python\Exercise_three.gdb\Tracts"

join_features = r"C:\Users\atohtson\Desktop\Exercise_3_Working_20FEB19\Exercise3\Example_3_Python\Exercise_three.gdb\CallsforService"

out_feature_class = r"C:\Users\atohtson\Desktop\Exercise_3_Working_20FEB19\Exercise3\Example_3_Python\Exercise_three.gdb\Tracts_Calls"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)

print ( "All done")




