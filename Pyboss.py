import csv
import datetime

# Files
file_load = "employee_data1.csv"
file_output = "employee_data_reformatted2.csv"

# Dictionary
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Empty Lists
empty_ids = []
empty_ssn = []
empty_first = []
empty_last = []
empty_states = []
empty_dobs = []

with open(file_load) as df:
    reader = csv.DictReader(df)

    for row in reader:

        # reformat  social
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)

        empty_ssn = empty_ssn + [joined_ssn]

        #reformat state
        state_in = us_state_abbrev[row["State"]]
        empty_states = empty_states + [state_in]

        empty_ids = empty_ids + [row["Emp ID"]]

        #reformat IDs
        splitname = row["Name"].split(" ")
        empty_first = empty_first + [splitname[0]]
        empty_last = empty_last + [splitname[1]]

        #reformat dob
        new_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        new_dob = new_dob.strftime("%m/%d/%Y")
        empty_dobs = empty_dobs + [new_dob]

# Zip file
empty_db = zip(empty_ids, empty_first, empty_last,
            empty_dobs, empty_ssn, empty_states)

# Write all of the election data to csv
with open(file_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Empty ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empty_db)
