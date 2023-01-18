import csv
import json

my_list = []

with open('diseases.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Disease = row["Disease"]
        Symptoms = [    
            " ".join(row["Symptom_1"].split("_")),
            " ".join(row["Symptom_2"].split("_")),
            " ".join(row["Symptom_3"].split("_")),
            " ".join(row["Symptom_4"].split("_")),
            " ".join(row["Symptom_5"].split("_")),
            " ".join(row["Symptom_6"].split("_")),
            " ".join(row["Symptom_7"].split("_")),
            " ".join(row["Symptom_8"].split("_")),
            " ".join(row["Symptom_9"].split("_")),
            " ".join(row["Symptom_10"].split("_")),
            " ".join(row["Symptom_11"].split("_")),
            " ".join(row["Symptom_12"].split("_")),
            " ".join(row["Symptom_13"].split("_")),
            " ".join(row["Symptom_14"].split("_")),
            " ".join(row["Symptom_15"].split("_")),
            " ".join(row["Symptom_16"].split("_")),
            " ".join(row["Symptom_17"].split("_")),

        ]
        my_list.append({"Disease": Disease , "Symptoms": Symptoms})

intents = {"intents": my_list}
with open('dataset.json', 'w') as outfile:
    json.dump(intents, outfile, indent= 4)