# Medical Wordlist

Medical wordlists in English, French, and Ukrainian languages, which can be used for spell checking. This project is based on collection of SPARQL requests using Wikidata Query Service.

## Getting Started

You can find all medical words by language in the following files:
- fr/wordlist.fr.txt : 20622 words
- en/wordlist.en.txt : 164450 words
- uk/wordlist.uk.txt : 4687 words

To contribute and add more medical keywords, you can make a merge request.

## Contributions

Contributions are welcome to advance this project and create a comprehensive taxonomy of medicine in the future (using wikidata-taxonomy). If you would like to contribute, please follow these steps:

- Fork the repository and create a new branch for your contribution.
- Add the new medical keywords to the appropriate language file(s).
- Create a pull request.

We appreciate any contributions to this project.

## Script

The generate-wordlist-txt.sh command allows you to assemble multiple files containing keyword lists for spell checking from a specific language folder (en, fr, uk). It then sorts the keywords alphabetically and removes all duplicate keywords. The final result is a single file containing all the sorted and unique keywords. This command is useful for consolidating multiple sources of keywords into a single list for use as a reference in spelling correction processes.

## License

This project is licensed under the Do What The F*ck You Want To Public License.

## Acknowledgments

- [Wikidata Query Service](https://query.wikidata.org)
