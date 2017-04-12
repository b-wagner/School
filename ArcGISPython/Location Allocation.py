# Import arcpy module
import arcpy

def LoadFacilities():
    

    # Local variables:
    Location_Allocation = "Location-Allocation"
    Location_Allocation__2_ = Location_Allocation
    #Having issues with this, check data type
    BG15_Tiger_NE_SD_BA_Data_PNT = arcpy.GetParameterAsText(0)
    

    arcpy.SelectLayerByAttribute_management(arcpy.MakeTableView_management(BG15_Tiger_NE_SD_BA_Data_PNT, "Table"), "NEW_SELECTION", ' "FacType_NE" = 0 ')

    # Process: Add Locations
    arcpy.AddLocations_na(Location_Allocation, "Facilities", BG15_Tiger_NE_SD_BA_Data_PNT, "Name GEOID #;FacilityType FacType_NE #", "5 Miles", "", "NE_SD_Roads2016 SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "NE_SD_Roads2016 #;Roads_ND_Junctions #")
    return

def LoadDemandPoints():
    
    arcpy.SelectLayerByAttribute_management("BG15_Tiger_NE_SD_BA_Data_PNT", "CLEAR_SELECTION")

    # Local variables:
    Location_Allocation = "Location-Allocation"
    Location_Allocation__2_ = Location_Allocation
    BG15_Tiger_NE_SD_BA_Data_PNT = "BG15_Tiger_NE_SD_BA_Data_PNT"

    # Process: Add Locations
    arcpy.AddLocations_na(Location_Allocation, "Demand Points", BG15_Tiger_NE_SD_BA_Data_PNT, "Name GEOID #;Weight TOTPOP_CY #", "5 Miles", "", "NE_SD_Roads2016 SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "NE_SD_Roads2016 #;Roads_ND_Junctions #")
    return

def MakeLocationAllocationLayer():

    # Local variables:
    #Roads_ND = "Roads_ND"
    Roads_ND = arcpy.GetParameterAsText(1);
    Location_Allocation = "Location-Allocation"

    # Process: Make Location-Allocation Layer
    arcpy.MakeLocationAllocationLayer_na(Roads_ND, "Location-Allocation", "Minutes", "FACILITY_TO_DEMAND", "MINIMIZE_IMPEDANCE", "1", "", "LINEAR", "1", "10", "", "ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY", "", "NO_HIERARCHY", "STRAIGHT_LINES", "1", "")
    return       
    
def SetSolverProperties():

    solverProps = arcpy.na.GetSolverProperties(arcpy.mapping.Layer("Location-Allocation"))
    solverProps.impedance = 'Minutes'
    solverProps.uTurns = 'NO_UTURNS'
    solverProps.problemType = 'MAXIMIZE_COVERAGE'
    solverProps.facilitiesToFind = 17
    solverProps.accumulators = 'Minutes'
    solverProps.impedanceCutoff = 100
    return

def SolveLocationAllocation():

    # Local variables:
    Location_Allocation = "Location-Allocation"
    Location_Allocation__2_ = Location_Allocation
    Solve_Succeeded = "false"

    # Process: Solve
    arcpy.Solve_na(Location_Allocation, "SKIP", "TERMINATE", "")
    return

MakeLocationAllocationLayer()
LoadFacilities()
LoadDemandPoints()
SetSolverProperties()
SolveLocationAllocation()





