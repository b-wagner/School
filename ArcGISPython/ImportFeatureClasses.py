import arcpy
import os

arcpy.env.workspace = "E:/NE_SD_UTM14N.gdb"

blockGroups = "BG15_Tiger_NE_SD_BA_Data"
roads = "NE_SD_Roads2016"
counties = "NE_SD_Counties"
places = "NE_SD_Places"
stateBoundaries = "NE_SD_StateBoundaries"
schools = "NE_Schools"

outFeatureClass = os.path.join("F:/Data/Automated_Project.gdb/")

arcpy.CopyFeatures_management(blockGroups, outFeatureClass + blockGroups)
arcpy.CopyFeatures_management(roads, outFeatureClass + roads)
arcpy.CopyFeatures_management(places, outFeatureClass + places)
arcpy.CopyFeatures_management(stateBoundaries, outFeatureClass + stateBoundaries)
arcpy.CopyFeatures_management(schools, outFeatureClass + schools)
