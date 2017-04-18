import arcpy
import datetime

time = datetime.datetime.now().time()

mxd = arcpy.mapping.MapDocument("CURRENT")
dataframe = arcpy.mapping.ListDataFrames(mxd, "*")[0]

BG15_Tiger_NE_SD_BA_Data_PNT = arcpy.GetParameterAsText(0)
Roads_ND = arcpy.GetParameterAsText(1)

arcpy.mapping.AddLayer(dataframe, arcpy.mapping.Layer(BG15_Tiger_NE_SD_BA_Data_PNT))

tableView = arcpy.MakeTableView_management(BG15_Tiger_NE_SD_BA_Data_PNT, "Table" + str(time))
Location_Allocation = "Location-Allocation2"

def LoadFacilities():
    arcpy.SelectLayerByAttribute_management(tableView, "NEW_SELECTION", ' "FacType_NE" = 0 ')

    # Process: Add Locations
    arcpy.AddLocations_na(Location_Allocation, "Facilities", tableView,
                          "Name GEOID #;FacilityType FacType_NE #", "5 Miles", "",
                          "NE_SD_Roads2016 SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP",
                          "5 Meters", "INCLUDE", "NE_SD_Roads2016 #;Roads_ND_Junctions #")
    return


def LoadDemandPoints():
    arcpy.SelectLayerByAttribute_management(tableView, "NEW_SELECTION", "GEOID LIKE '31%'")

    # Process: Add Locations
    arcpy.AddLocations_na(Location_Allocation, "Demand Points", tableView,
                          "Name GEOID #;Weight TOTPOP_CY #", "5 Miles", "",
                          "NE_SD_Roads2016 SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP",
                          "5 Meters", "INCLUDE", "NE_SD_Roads2016 #;Roads_ND_Junctions #")
    return


def MakeLocationAllocationLayer():
    # Process: Make Location-Allocation Layer
    arcpy.MakeLocationAllocationLayer_na(Roads_ND, "Location-Allocation", "Minutes", "FACILITY_TO_DEMAND",
                                         "MINIMIZE_IMPEDANCE", "1", "", "LINEAR", "1", "10", "",
                                         "ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY", "", "NO_HIERARCHY", "STRAIGHT_LINES",
                                         "1", "")

    return

def SetSolverProperties():
    solverProps = arcpy.na.GetSolverProperties(arcpy.mapping.Layer(Location_Allocation))
    solverProps.impedance = 'Minutes'
    solverProps.uTurns = 'NO_UTURNS'
    solverProps.problemType = 'MAXIMIZE_COVERAGE'
    solverProps.facilitiesToFind = 17
    solverProps.accumulators = 'Minutes'
    solverProps.impedanceCutoff = 100
    return


def SolveLocationAllocation():
    Solve_Succeeded = "false"

    # Process: Solve
    arcpy.Solve_na(Location_Allocation, "SKIP", "TERMINATE", "")
    return


#MakeLocationAllocationLayer()
LoadFacilities()
LoadDemandPoints()
SetSolverProperties()
SolveLocationAllocation()





