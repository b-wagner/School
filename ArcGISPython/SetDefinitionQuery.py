import arcpy

state = arcpy.GetParameterAsText(0)

# Set current map and store layers in dataframe to list
mxd = arcpy.mapping.MapDocument("CURRENT")
fc = arcpy.mapping.ListLayers(mxd)

counter = 0

while counter < len(fc):

    fields = arcpy.ListFields(fc[counter])

    # This loop iterates through all the field names in
    # each feature class's attribute table, then sets
    # the appropriate values.
    for x in fields:
        if x.name == "STATEFP":
            fc[counter].definitionQuery = "STATEFP = '" + state + "'"
        elif x.name == "GEOID":
            fc[counter].definitionQuery = "GEOID LIKE '" + state + "%'"

    counter += 1

    arcpy.RefreshActiveView()

print "Definition queries set to only include data from the state of Nebraska."
