import requests
import argparse
import os

parser = argparse.ArgumentParser(description='Execute a SPARQL query on Wikidata Query Service and save the results to a file')
parser.add_argument('query_file', type=str, help='the file containing the SPARQL query')
parser.add_argument('output_file', type=str, nargs='?', help='the file to save the results to')
args = parser.parse_args()

with open(args.query_file, 'r') as f:
    query = f.read()

params = {
    'query': query,
    'format': 'json'
}

response = requests.get('https://query.wikidata.org/sparql', params=params)

if response.status_code == 200:
    data = response.json()
    results = data['results']['bindings']

    if not args.output_file:
        base_name = os.path.basename(args.query_file)
        output_file = os.path.splitext(base_name)[0] + ".txt"
    else:
        output_file = args.output_file

    with open(output_file, 'w') as out:
        for result in results:
            label = result['label']['value']
            out.write(label + '\n')
else:
    print('Error executing SPARQL query. Response code:', response.status_code)