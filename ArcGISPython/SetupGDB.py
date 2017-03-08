import arcpy

#Sets this to current workspace
arcpy.env.workspace = "F:/Data"

#Variables for path and geodatabase name
gdb_path = "F:/Data"
gdb_name = "Automated_Project.gdb"

#Create the file geodatabase
arcpy.CreateFileGDB_management(gdb_path, gdb_name)

print gdb_name + " created at " + gdb_path