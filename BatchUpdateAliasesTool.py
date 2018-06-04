import arcpy
import csv

###### INPUTS:

# Establish parameter to be entered by user: Input feature class (or table)
infc = arcpy.GetParameterAsText(0)

# Establish parameter to be entered by user: Input csv file which should contain:
# field names to be updated in the first column, and
# corresponding aliases in the second column
in_csv = arcpy.GetParameterAsText(1)

######

# Establish empty master alias list to contain pairs of field and corresponding alias
field_alias_list = []

# Open and read csv containing field names to be updated
with open(in_csv, 'rb') as csvfile:
    alias_csv = csv.reader(csvfile)

# Loop through each row in csv. For each row, create list with 2 items in the following format:
# ['field_name','field alias']
    for row in alias_csv:
        pair_list = []
        field_value = row[0]
        alias_value = row[1]
        pair_list.append(field_value)
        pair_list.append(alias_value)

    # append each pair list to the master alias list
        field_alias_list.append(pair_list)

# Loop through master alias list
for field in field_alias_list:

    # For each pair of field name and alias, establish field name variable and alias variable
    field_name = (field[0])
    field_alias = (field[1])

    # test whether field name exists in the FC/table. If it does exist, update it with the
    # corresponding alias value, and display message that alias was updated
    if field_name in [field.name for field in arcpy.ListFields(infc)]:
        arcpy.AlterField_management(infc, field_name, new_field_alias = field_alias)
        arcpy.AddMessage("Alias updated for field " + field_name)

    # if field name does not exist in FC/table, display appropriate message
    else:
        arcpy.AddMessage("Table does not contain field " + field_name + "; alias not updated")
