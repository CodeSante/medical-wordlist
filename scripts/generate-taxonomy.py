import requests
import json
import unidecode

# Requête pour récupérer les informations sur les maladies et leur domaine médical de Wikidata
url = "https://query.wikidata.org/sparql"
query = """
SELECT ?item ?itemLabel ?medical_specialty ?medical_specialtyLabel ?subclass_of ?subclass_ofLabel
WHERE
{
  ?item wdt:P31 wd:Q12136.
  ?item wdt:P1995 ?medical_specialty.
  OPTIONAL { ?item wdt:P279 ?subclass_of. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ua". }
}
ORDER BY ?medical_specialtyLabel ?subclass_ofLabel ?itemLabel
"""
headers = {"Accept": "application/json"}
response = requests.get(url, params={"query": query}, headers=headers)
response.raise_for_status()

# Analyse des résultats de la requête et stockage des informations dans une structure de données
data = response.json()
taxonomy = {}
for item in data["results"]["bindings"]:
    item_id = item["item"]["value"].split("/")[-1]
    item_label = item["itemLabel"]["value"]
    item_label = unidecode.unidecode(item_label)  # Conversion des caractères Unicode en ASCII
    medical_specialty_id = item["medical_specialty"]["value"].split("/")[-1]
    medical_specialty_label = item["medical_specialtyLabel"]["value"]
    medical_specialty_label = unidecode.unidecode(medical_specialty_label)  # Conversion des caractères Unicode en ASCII
    if medical_specialty_id not in taxonomy:
        taxonomy[medical_specialty_id] = {
            "label": medical_specialty_label,
            "children": {}
        }
    if "subclass_of" in item:
        subclass_of_id = item["subclass_of"]["value"].split("/")[-1]
        subclass_of_label = item["subclass_ofLabel"]["value"]
        subclass_of_label = unidecode.unidecode(subclass_of_label)  # Conversion des caractères Unicode en ASCII
        if subclass_of_id not in taxonomy[medical_specialty_id]["children"]:
            taxonomy[medical_specialty_id]["children"][subclass_of_id] = {
                "label": subclass_of_label,
                "children": []
            }
        taxonomy[medical_specialty_id]["children"][subclass_of_id]["children"].append({"id": item_id, "label": item_label})
    else:
        if "Other" not in taxonomy[medical_specialty_id]["children"]:
            taxonomy[medical_specialty_id]["children"]["Other"] = {
                "label": "Other",
                "children": []
            }
        taxonomy[medical_specialty_id]["children"]["Other"]["children"].append({"id": item_id, "label": item_label})

# Tri de la taxonomie par ordre alphabétique
for medical_specialty_id in taxonomy:
    taxonomy[medical_specialty_id]["children"] = dict(sorted(taxonomy[medical_specialty_id]["children"].items(), key=lambda x: x[1]["label"]))
    for subclass_of_id in taxonomy[medical_specialty_id]["children"]:
        taxonomy[medical_specialty_id]["children"][subclass_of_id]["children"] = sorted(taxonomy[medical_specialty_id]["children"][subclass_of_id]["children"], key=lambda x: x["label"])

# Écriture de la taxonomie au format JSON dans un fichier
with open("taxonomy.json", "w") as outfile:
    json.dump(taxonomy, outfile, indent=4)
