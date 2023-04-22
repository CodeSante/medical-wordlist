# Medical Wordlist

Medical wordlists in English, French, and Ukrainian languages, which can be used for spell checking. This project is based on collection of SPARQL requests using Wikidata Query Service.

## Getting Started

You can find all medical words by language in the following files:
- fr/wordlist.fr.txt : 23384 words
- en/wordlist.en.txt : 171696 words
- ua/wordlist.ua.txt : 5187 words

To contribute and add more medical keywords, you can make a merge request.

## Contributions

Contributions are welcome to advance this project and create a comprehensive taxonomy of medicine in the future (using wikidata-taxonomy). If you would like to contribute, please follow these steps:

- Fork the repository and create a new branch for your contribution.
- Add the new medical keywords to the appropriate language file(s).
- Create a pull request.

We appreciate any contributions to this project.

## Scripts

The **generate-wordlist-txt.sh** command allows you to assemble multiple files containing keyword lists for spell checking from a specific language folder (en, fr, ua). It then sorts the keywords alphabetically and removes all duplicate keywords. The final result is a single file containing all the sorted and unique keywords. This command is useful for consolidating multiple sources of keywords into a single list for use as a reference in spelling correction processes.

The **launcher-sparql-query.py** script executes a SPARQL query on Wikidata Query Service and saves the results to a file. The user provides the path to the file containing the SPARQL query as well as the path to the file where the results will be saved. The script reads the query from the input file, sends it to Wikidata Query Service, and retrieves the results in JSON format. If the query is successful, the script extracts the desired data from the JSON results and writes it to the output file. If there is an error, the script prints an error message along with the response code.

The **update-sparql-query.sh** script takes a command-line argument -d to specify the directory containing all the SPARQL queries to be executed. The script generates the output files with a .txt extension using _launcher-sparql-query.py_ script. For example, to execute the script on SPARQL queries located in the sparql/fr directory, run the command :

```bash
bash update-sparql-directory.sh -d sparql/fr
```
The output files will be generated in the current directory.

## ⚠️  Project in progress

- SPARQL queries must be reworked
- This project does not come from a collaboration with the medical world
- The keywords are all in lower case

## License

This project is licensed under the Do What The F*ck You Want To Public License.

## Acknowledgments

- [Wikidata Query Service](https://query.wikidata.org)
- [glutanimate/wordlist-medicalterms-en](https://github.com/glutanimate/wordlist-medicalterms-en)
