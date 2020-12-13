# !Python3
# read_census_excel.py - Tabulates the population and number of census tracts of each county

import openpyxl, pprint
from pathlib import Path

wb = openpyxl.load_workbook(Path.cwd() / 'spreadsheets/censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

print("Reading rows...")
for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Remember what setdefault does
    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)

print("Writing the results...")
result_file = open('spreadsheets/census2010.py', 'w+')
result_file.write('allData = ' +pprint.pformat(county_data))
result_file.close()
print("Done!")

# To use the info just use:
# import os
# from spreadsheets import census2010
# census2010.allData['AK']['Anchorage']

