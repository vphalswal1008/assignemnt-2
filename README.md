# PubMed Paper Fetcher  

## Overview  
This command-line program fetches research papers from PubMed based on a user-provided query. It filters results for pharmaceutical/biotech affiliations and either prints them to the console or saves them to a CSV file.  

## Code Organization  
```
pubmedDataFromQuery/
  ├── main.py  # The main script containing the logic to fetch and filter PubMed papers.
README.md       # This file, providing instructions and details about the program.
pyproject.toml  # Configuration file for dependency management using poetry.
```

## Installation  

### Prerequisites  
Ensure you have Python installed (Python 3.9 or later is required). Install [Poetry](https://python-poetry.org/) if you haven't already:  

```sh
pip install poetry
```

### Install Dependencies  
Run the following command inside the project directory:  

```sh
poetry install
```

## Execution  

### Using Poetry  
To run the script, use:  

```sh
poetry run python pubmedDataFromQuery/main.py "your_query"
```

Example:  

```sh
poetry run python pubmedDataFromQuery/main.py "oral cavity cancer"
```

### Optional Arguments  
- `-h` or `--help`: Display usage instructions.  

  ```sh
  poetry run python pubmedDataFromQuery/main.py -h
  ```

- `-d` or `--debug`: Print debug information during execution.  

  ```sh
  poetry run python pubmedDataFromQuery/main.py "oral cavity cancer" -d
  ```

- `-f` or `--file`: Specify a filename to save results instead of printing them.  

  ```sh
  poetry run python pubmedDataFromQuery/main.py "oral cavity cancer" -f results.csv
  ```

## Tools & Libraries Used  
- **[Biopython](https://biopython.org/)**: Used to interact with the PubMed API.  
- **Python argparse**: Built-in library for handling command-line arguments.  

## Contact  
For any issues or contributions, feel free to reach out!