"""
HTML parser using BeautifulSoup.
When you want to parse HTML the easy way.
"""

from typing import List, Dict
from bs4 import BeautifulSoup

PARSER_BACKEND = "html.parser"

class BeautifulSoupParser:
    """Just use BeautifulSoup. It's solid."""
    
    def __init__(self, html_text: str):
        """Pass the HTML string."""
        self.html_text = html_text
        self.soup = BeautifulSoup(html_text,PARSER_BACKEND)
    
    def parse(self) -> Dict[str, any]:
        """Extract hrefs and classes. Return a dict."""
        
        result = {
            "href_links": self.extract_hrefs(),
            "anchor_classes": self.extract_anchor_classes()
        }
            
        return result
    
    def extract_hrefs(self) -> List[str]:
        """Get all hrefs from <a> tags."""
        hrefs = []
        
        # Find all <a> tags and pull out the href
        for link in self.soup.find_all('a', href=True):
            hrefs.append(link['href'])
        
        return hrefs
    
    def extract_anchor_classes(self) -> List[str]:
        """Get class values from anchor tags."""
        classes = []
        
        # Go through each <a> tag and grab classes if they exist
        for link in self.soup.find_all('a'):
            if link.get('class'):
                # BeautifulSoup returns class as a list
                class_value = ' '.join(link.get('class'))
                classes.append(class_value)
        
        return classes
    
    def get_soup_object(self):
        """Get the raw soup object if you need to dig deeper."""
        return self.soup
    
    def pretty_print(self) -> str:
        """Get nicely formatted HTML."""
        return self.soup.prettify()
