import json


new_list =[]
diseases = []

with open('dataset.json','r+') as f :
    data = json.load(f)
    old_list = data["intents"]
    for disease in old_list:
        new_symptoms = []
        clubbedsymptoms = ""
        old_symptoms = disease["Symptoms"]
        for symptom in old_symptoms:
            if(symptom != ""):
                
                new_symptoms.append(symptom)
        if disease["Disease"] not in diseases:
            
            clubbedsymptoms = " ".join(new_symptoms)
            new_symptoms.append(clubbedsymptoms)
            
            new_list.append({"Disease": disease["Disease"], "Symptoms": [clubbedsymptoms]})
        diseases.append(disease["Disease"]) 
intents = {"intents": new_list}
with open('dataset1.json', 'w') as outfile:
    json.dump(intents, outfile, indent= 4)
