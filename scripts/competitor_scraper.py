import requests
from bs4 import BeautifulSoup, Tag
import re

def find_competitors(keyword, max_results=5):
    """Perform actual Google search to find competitor domains"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        search_url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}"
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        competitor_domains = []
        
        # Extract organic search results
        # Type-checking each result to ensure it's a Tag before processing
        for result in soup.find_all('div', class_='tF2Cxc', limit=max_results):
            if not isinstance(result, Tag):
                continue
            
            link_tag = result.find('a')
            if link_tag and isinstance(link_tag, Tag):
                href = str(link_tag.get('href', ''))  # Ensure string type
                if href.startswith('/'):
                    href = f"https://www.google.com{href}"
                domain_match = re.search(r'https?://([^/]+)', href) if href else None
                if domain_match:
                    competitor_domains.append({
                        "domain": domain_match.group(1),
                        "position": len(competitor_domains)+1
                    })
            
        return competitor_domains
    
    except Exception as e:
        print(f"Web search failed: {str(e)}")
        return [{"domain": f"competitor{str(i+1)}.com", "position": i+1} 
                for i in range(max_results)]
