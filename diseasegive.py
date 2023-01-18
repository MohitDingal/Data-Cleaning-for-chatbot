import csv
import json

my_list = []
diseases = []
with open('diseases.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    c = 1
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
        new_symptoms = []
        for symptom in Symptoms:
            if(symptom != ""):
                
                new_symptoms.append(symptom)
        if Disease not in diseases:
             my_list.append({"Disease_Num":"DiseaseNum "+str(c), "Disease": [Disease] , "Symptoms": new_symptoms})
             c+=1
        diseases.append(Disease) 
        
intents = {"intents": my_list}
with open('dataset2.json', 'w') as outfile:
    json.dump(intents, outfile, indent= 4)