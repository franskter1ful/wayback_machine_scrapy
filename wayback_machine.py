import requests
from bs4 import BeautifulSoup

def search_for_element_inwayback_machine(url, element):
    wayback_api_url = f"http://archive.org/wayback/available?url={url}"
    
    response = requests.get(wayback_api_url)
    if response.status_code == 200:
        archived_versions = response.json().get('archived_snapshots')
        
        if archived_versions:
            for snapshot_url in archived_versions.values():
                snapshot_url = snapshot_url['url']
                snapshot_response = requests.get(snapshot_url)
                if snapshot_response.status_code == 200:
                    soup = BeautifulSoup(snapshot_response.content, 'html.parser')
                    found_element = soup.find(element)
                    if found_element:
                        print(f"Element '{element}' found in {snapshot_url}")
                        return found_element

    print(f"Element '{element}' not found in the Wayback Machine for {url }")
    return None

website_url = "https://oblong.com"
element_to_search = "input"

search_element_in_wayback_machine(website_url, element_to_search)