import csv
import json

my_list = []
medicine_names = []
with open('medicinefinal.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    c = 1
    for row in reader :
        # print(row)
        
        uses_list = row["Uses"].split(",")
        uses_list.pop()
        
        clubbed_uses = ""
        clubbed_uses = " ".join(uses_list)
        if len(uses_list) != 1:
            uses_list.append(clubbed_uses)
        if row["Medicine Name"] not in medicine_names:
            my_list.append({"Medicine_Number": "Medicine" + str(c), "Medicine Name": row["Medicine Name"], "Uses": uses_list, "Prescription": row["Prescription"], "MRP":  row["MRP"][1:] })
            c = c + 1
        medicine_names.append(row["Medicine Name"])

intents = {"intent": my_list}
with open('medicine4.json', 'w') as outfile:
    json.dump(intents, outfile, indent= 4)