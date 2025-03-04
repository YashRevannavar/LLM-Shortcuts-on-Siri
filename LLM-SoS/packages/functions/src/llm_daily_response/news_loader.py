import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List
from langchain_community.document_loaders import WebBaseLoader


def extract_headline_urls(url):
    """Fetch the given URL and extract all headline link URLs found on the page."""
    try:
        logging.info(f"Fetching URL: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    headline_links = set()

    for heading in soup.find_all(['h1', 'h2', 'h3']):
        a_tag = heading.find('a', href=True)
        if a_tag:
            href = a_tag['href']
            full_url = urljoin(url, href)
            headline_links.add(full_url)

    for a_tag in soup.find_all('a', href=True):
        attributes = " ".join(a_tag.get('class', [])) + " " + (a_tag.get('id') or "")
        attributes = attributes.lower()
        if any(keyword in attributes for keyword in ['headline', 'title']):
            href = a_tag['href']
            full_url = urljoin(url, href)
            headline_links.add(full_url)

    headline_urls = list(headline_links)
    logging.info(f"Extracted {len(headline_urls)} headline URLs from {url}")
    return headline_urls


def collect_top_headline_content(site_url:str, limit: int = 7) -> List[str]:
    """
    Fetch headlines from a given site URL, limit the number of results,
    load each page with WebBaseLoader, and return combined text
    (title + page content) for each page.
    """
    extracted_urls = extract_headline_urls(site_url)
    limited_urls = extracted_urls[:limit]
    loader = WebBaseLoader(limited_urls)
    data_items = loader.load()
    collected_data = []
    for item in data_items:
        title = item.metadata.get('title', '')
        page_text = item.page_content or ''
        truncated_text = page_text[:1500]  # Keep only 1000 chars of the content
        combined_text = f"{title} {truncated_text}".strip()
        collected_data.append(combined_text)
    logging.info(f"Collected {len(collected_data)} headline contents from {site_url}")
    return collected_data
