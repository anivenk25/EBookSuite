import requests
from bs4 import BeautifulSoup
import re

def search_pdfs(query):
    """
    Search for PDFs on the web using DuckDuckGo.
    """
    search_url = "https://html.duckduckgo.com/html/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    data = {"q": f"{query} filetype:pdf", "kl": "us-en"}  # Restrict to English results

    # Send search request
    response = requests.post(search_url, headers=headers, data=data)
    if response.status_code != 200:
        print(f"Error with search engine: {response.status_code}")
        return []

    # Parse results with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.endswith(".pdf") or "pdf" in href.lower():
            links.append(href)
    return links

def display_pdf_links(links):
    """
    Display the PDF links from search results.
    """
    print("\nSearch Results (PDFs):")
    if not links:
        print("No results found.")
        return
    for i, link in enumerate(links, start=1):
        print(f"{i}. {link}")

def main():
    # Input book title or ISBN
    query = input("Enter the book title or ISBN: ")

    # Search for PDFs
    pdf_links = search_pdfs(query)
    display_pdf_links(pdf_links)

if __name__ == "__main__":
    main()

