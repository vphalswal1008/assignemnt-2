import argparse
import csv
import re
from Bio import Entrez, Medline

def fetch_and_filter_papers(query, output_filename=None, debug=False):
    """
    Fetches research papers from PubMed based on a query, filters for
    pharmaceutical/biotech affiliations, and either prints results or saves to a CSV file.
    """
    if debug:
        print(f"[DEBUG] Query: {query}")
    
    Entrez.email = "your_email@example.com"  # Replace with your email

    # Search PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=200)
    record = Entrez.read(handle)
    handle.close()
    pubmed_ids = record["IdList"]

    if debug:
        print(f"[DEBUG] Found {len(pubmed_ids)} PubMed IDs")

    papers = []
    if pubmed_ids:
        handle = Entrez.efetch(db="pubmed", id=pubmed_ids, rettype="medline", retmode="text")
        records = Medline.parse(handle)

        pharma_keywords = ["pharmaceutical", "biotech", "biotechnology", "pharma", "drug", "life sciences"]
        university_keywords = ["university", "college", "institute", "school"]

        for record in records:
            pubmed_id = record.get("PMID", "N/A")
            title = record.get("TI", "No Title Available")
            authors = record.get("AU", [])
            abstract = record.get("AB", "No Abstract Available")
            journal = record.get("JT", "No Journal Available")
            pub_date = record.get("DP", "No Date Available")
            affiliations = record.get("AD", [])
            corresponding_email = "N/A"

            if not isinstance(affiliations, list):
                affiliations = [affiliations]

            email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            emails = [re.search(email_pattern, aff) for aff in affiliations if re.search(email_pattern, aff)]
            if emails:
                corresponding_email = emails[0].group()

            company_affiliations = [aff for aff in affiliations if any(keyword.lower() in aff.lower() for keyword in pharma_keywords)]
            non_academic_authors = [aff for aff in affiliations if not any(keyword.lower() in aff.lower() for keyword in university_keywords)]

            papers.append([
                pubmed_id, title, ", ".join(authors), pub_date, journal,
                "; ".join(non_academic_authors) if non_academic_authors else "N/A",
                "; ".join(company_affiliations) if company_affiliations else "N/A",
                corresponding_email
            ])

        handle.close()

    if output_filename:
        with open(output_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "PubMed ID", "Title", "Authors", "Publication Date", "Journal",
                "Non-academic Authors", "Company Affiliation(s)", "Corresponding Author Email"
            ])
            writer.writerows(papers)
        print(f"Saved {len(papers)} papers to {output_filename}")
    else:
        for paper in papers:
            print(paper)

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter PubMed papers based on a query.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results. If not provided, prints to console.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    
    args = parser.parse_args()
    fetch_and_filter_papers(args.query, args.file, args.debug)

if __name__ == "__main__":
    main()
