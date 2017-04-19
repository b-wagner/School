# Import arcpy module

import arcpy



# Local variables:


Roads_ND = arcpy.GetParameterAsText(0)


Location_Allocation = "Location-Allocation"


# Process: Make Location-Allocation Layer

arcpy.MakeLocationAllocationLayer_na(Roads_ND, "Location-Allocation", "Minutes", "FACILITY_TO_DEMAND", "MINIMIZE_IMPEDANCE", "1", "", "LINEAR", "1", "10", "", "ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY", "", "NO_HIERARCHY", "STRAIGHT_LINES", "1", "")

