# Import arcpy module
import arcpy


# Local variables:
Location_Allocation = "Location-Allocation"
Location_Allocation__2_ = Location_Allocation
Solve_Succeeded = "false"

# Process: Solve
arcpy.Solve_na(Location_Allocation, "SKIP", "TERMINATE", "")

