import arcpy

solverProps = arcpy.na.GetSolverProperties(arcpy.mapping.Layer("Location-Allocation"))
solverProps.impedance = 'Minutes'
solverProps.uTurns = 'NO_UTURNS'
solverProps.problemType = 'MAXIMIZE_COVERAGE'
solverProps.facilitiesToFind = 17
solverProps.accumulators = 'Minutes'

