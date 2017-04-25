import arcpy

gdb_path = arcpy.GetParameterAsText(0)

arcpy.env.workspace = gdb_path

#Get map document
mxd = arcpy.mapping.MapDocument("CURRENT")

#Get desired dataframe
dataframe = arcpy.mapping.ListDataFrames(mxd, "*")[0]

#Loop through feature classes and add all to dataframe
for fc in arcpy.ListFeatureClasses():
    arcpy.mapping.AddLayer(dataframe, arcpy.mapping.Layer(gdb_path + "/"+fc))

print "Feature classes sucessfully added to dataframe."