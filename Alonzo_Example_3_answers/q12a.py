featureClass = r'C:\Users\atohtson\Desktop\Exercise_3_Working_18FEB19\Exercise3\Example_3_Python\Exercise_three.gdb\General_Offense'
fieldNames = ['primary_key', 'occ_dt', 'obfAddress', 'x_rand', 'y_rand','disclaimer', 'place_name','OffenseCustom','locationTranslation']
cursorFields = ','.join(fieldNames)

arcpy.MakeFeatureLayer_management (inFeatures,'General_Offense_lyr') 

arcpy.SelectLayerByAttribute_management('General_Offense_lyrr','NEW_SELECTION',"OffenseCustom = 'BURGLARY FORCE                ' And locationTranslation = 'Residence/Home''")

arcpy.CopyFeatures_management('CallsforService_lyr',r'C:\Users\atohtson\Desktop\Exercise_3_Working_18FEB19\Exercise3\Example_3_Python\Exercise_three.gdb\Burglary_Residence')

fcList = arcpy.ListFeatureClasses()
with open('codes.csv', 'wb') as f:
     writer = csv.writer(f)
     writer.writerows(fcList)

     
print('Created csv file')