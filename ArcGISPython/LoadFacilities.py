#NOTE - remember to add functionality to select records needed for facilities

# Import arcpy module
import arcpy

arcpy.SelectLayerByAttribute_management("BG15_Tiger_NE_SD_BA_Data_PNT", "NEW_SELECTION", ' "FacType_NE" = 0 ')

# Local variables:
Location_Allocation = "Location-Allocation"
Location_Allocation__2_ = Location_Allocation
BG15_Tiger_NE_SD_BA_Data_PNT = "BG15_Tiger_NE_SD_BA_Data_PNT"

# Process: Add Locations
arcpy.AddLocations_na(Location_Allocation, "Facilities", BG15_Tiger_NE_SD_BA_Data_PNT, "Name GEOID #;FacilityType FacType_NE #", "5 Miles", "", "NE_SD_Roads2016 SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "NE_SD_Roads2016 #;Roads_ND_Junctions #")

