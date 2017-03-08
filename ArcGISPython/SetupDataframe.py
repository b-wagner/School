import arcpy

gdb_path = "F:/Data"
gdb_name = "Automated_Project.gdb"

arcpy.env.workspace = gdb_path + "/" + gdb_name

#Get map document
mxd = arcpy.mapping.MapDocument("CURRENT")

#Get desired dataframe
dataframe = arcpy.mapping.ListDataFrames(mxd, "*")[0]

#Loop through feature classes and add all to dataframe
for fc in arcpy.ListFeatureClasses():
    arcpy.mapping.AddLayer(dataframe, arcpy.mapping.Layer(gdb_path + "/" + gdb_name + "/"+fc))

print "Feature classes sucessfully added to dataframe."
