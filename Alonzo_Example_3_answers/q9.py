import arcpy

#this is all my variables
currentworkspace = r'C:\Users\atohtson\Desktop\Exercise3\Example_3_Python\Exercise 3.gdb'
geometryType = 'POLYGON'
spatialRef = arcpy.SpatialReference(26949)

#this is the list of feature classes i want to create
featureClassNameList = ['Road']
arcpy.env.workspace = currentworkspace
arcpy.env.overwriteOutput = True

def creatFeatureClass(inFeatureClassName):
    arcpy.CreateFeatureclass_management(currentworkspace
                                        ,inFeatureClassName
                                        ,geometryType
                                        ,''
                                        ,'DISABLED'
                                        ,'DISABLED'
                                        ,spatialRef)
    print('created feature class called' + inFeatureClassName)


for fc in featureClassNameList:
    creatFeatureClass(fc)
    
creatFc = [creatFeatureClass(fc) for fc in featureClassNameList]

print (creatFc)

#create field
inFeatures = 'Road'
fieldname = 'NewField'
field_type = 'text'


arcpy.AddField_management (inFeatures, fieldname, 'text')
featureClass = r'C:\Users\atohtson\Desktop\Exercise3\Example_3_Python\Exercise 3.gdb\Road'

print ('field created')

 # add domain
domName= 'NewDomain'
gdb = currentworkspace
inFeatures = featureClass
inField = fieldname

 #create value domain

arcpy.CreateDomain_management(gdb, domName,'These are road types','text','CODED')

domDict={"1":"Asphalt","2":"Concrete","3":"Composite","4":"Gravel","5":"Dirt"}

for code in domDict:
       arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

arcpy.AssignDomainToField_management(inFeatures, inField, domName)

print ("Success")









