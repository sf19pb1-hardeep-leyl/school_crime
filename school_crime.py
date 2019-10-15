"""
Use a collections.Counter to count the crimes by borough.
Created: 2019-10-09
Dataset: https://data.cityofnewyork.us/Education/2017-2018-Schools-NYPD-Crime-Data-Report/kwvk-z7i9/data
"""

import sys
import collections
import pandas as pd

url = "https://data.cityofnewyork.us/api/views/kwvk-z7i9/rows.csv"

try:
    df = pd.read_csv(url)   #df is a pandas DataFrame.
except BaseException as error:
    print(error, file = sys.stderr)
    sys.exit(1)

#Only count schools where the "No Crim N" column is not 0
df_filtered = df.where( df["NoCrim N"] > 0 )

#d is a dictionary containing 5 keys and 5 values.
#Each key is a one-character string, and each value is an int.
d = collections.Counter(df_filtered["Borough"])

newNames = {
    "K": "Brooklyn",
    "M": "Manhattan",
    "Q": "Queens",
    "R": "Staten Island",
    "X": "Bronx"
}

#Dictionary comprehension: the new dictionary newd has the same content as d,
#except that each key is a name instead of just an initial.
newd = {newNames[key]: value for key, value in d.items()}

print("""\
2017 - 2018 Schools NYPD Crime Data Report
Source:
https://data.cityofnewyork.us/Education/2017-2018-Schools-NYPD-Crime-Data-Report/kwvk-z7i9/data

Counts by Borough
""")

for boro in sorted(newd):   #alphabetical order
    print(f"{newd[boro]:3} {boro}")

sys.exit(0)
