import csv
import json

my_list = []
medicine_names = []
with open('medicinefinal.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    c = 1
    for row in reader:
        # print(row)
        
        uses_list = row["Uses"].split(",")
        uses_list.pop()
        if row["Medicine Name"] not in medicine_names:
            my_list.append({"Medicine_Number": "Medicine" + str(c), "Medicine Name": [row["Medicine Name"]], "Uses": uses_list, "Prescription": row["Prescription"], "MRP":  row["MRP"][1:] })
            c = c + 1
        medicine_names.append(row["Medicine Name"])

intents = {"intent": my_list}
with open('medicine.json', 'w') as outfile:
    json.dump(intents, outfile, indent= 4)