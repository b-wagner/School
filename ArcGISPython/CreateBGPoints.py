import arcpy

gdb_path = "F:/Data"
gdb_name = "Automated_Project.gdb"

workspace = arcpy.env.workspace = gdb_path + "/" + gdb_name

# Add feature class to dataframe if not already
#mxd = arcpy.mapping.MapDocument("CURRENT")
#dataframe = arcpy.mapping.ListDataFrames(mxd, "*")[0]
#blockGroups = arcpy.mapping.AddLayer(dataframe, arcpy.mapping.Layer(gdb_path + "/" + gdb_name + "/BG15_Tiger_NE_SD_BA_Data"))

blockGroups = "BG15_Tiger_NE_SD_BA_Data"

# Feature to Point
arcpy.FeatureToPoint_management(blockGroups, "BG_Points")

print "Block group points successfully created."
