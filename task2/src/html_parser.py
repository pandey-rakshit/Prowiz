import re
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class HTMLElement:
    """A simple HTML element with its tag, attributes, and children."""
    tag: str
    attributes: Dict[str, str]
    content: str = ""
    children: List["HTMLElement"] = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []


class RecursiveHTMLParser:
    """Parse HTML using regex and recursion. No deps needed."""
    
    def __init__(self, html_text: str):
        """
        Initialize the parser with HTML text.
        
        Args:
            html_text: The HTML content as a string.
        """
        self.html_text = html_text
    
    def parse(self) -> Dict[str, any]:
        """
        Parse the HTML and extract href links and class attributes.
        
        Returns:
            Dictionary containing extracted data.
        """
        
        result = {
            "href_links": self._extract_hrefs(),
            "anchor_classes": self._extract_anchor_classes()
        }
        
        return result
    
    def _extract_hrefs(self) -> List[str]:
        """Find all href="..." in the HTML."""
        # a simple regex to grab all href values
        href_pattern = r'href\s*=\s*["\']([^"\']*)["\']'
        matches = re.findall(href_pattern, self.html_text, re.IGNORECASE)
        return matches
    
    def _extract_anchor_classes(self) -> List[str]:
        """Get class values from all <a> tags."""
        # Find all <a> tags with their attributes
        anchor_pattern = r'<a\s+([^>]*)>'
        anchor_matches = re.findall(anchor_pattern, self.html_text, re.IGNORECASE)
        
        classes = []
        class_pattern = r'class\s*=\s*["\']([^"\']*)["\']'
        
        for attributes in anchor_matches:
            class_matches = re.findall(class_pattern, attributes, re.IGNORECASE)
            classes.extend(class_matches)
        
        return classes
    
    def parse_tree(self) -> HTMLElement:
        """
        Build a tree structure of the HTML document recursively.
        
        Returns:
            Root HTMLElement representing the parsed HTML tree.
        """
        root, _ = self._parse_element(self.html_text, 0)
        return root
    
    def _parse_element(self, html: str, pos: int) -> tuple:
        """
        Recursively parse an HTML element starting at position pos.
        
        Args:
            html: The HTML text to parse.
            pos: Current position in the HTML text.
        
        Returns:
            Tuple of (parsed_element, new_position).
        """
        # Find the next tag
        tag_start = html.find('<', pos)
        
        if tag_start == -1:
            return None, len(html)
        
        # Extract tag content
        tag_end = html.find('>', tag_start)
        if tag_end == -1:
            return None, len(html)
        
        tag_content = html[tag_start + 1:tag_end]
        
        # Check if it's a closing tag
        if tag_content.startswith('/'):
            return None, tag_end + 1
        
        # Parse tag name and attributes
        tag_name = tag_content.split()[0].lower()
        attributes = self._extract_attributes(tag_content)
        
        element = HTMLElement(tag=tag_name, attributes=attributes)
        current_pos = tag_end + 1
        
        # Parse children until closing tag
        while current_pos < len(html):
            next_tag_start = html.find('<', current_pos)
            
            if next_tag_start == -1:
                break
            
            # Check if it's closing tag
            next_tag_end = html.find('>', next_tag_start)
            next_tag_content = html[next_tag_start + 1:next_tag_end]
            
            if next_tag_content.startswith(f'/{tag_name}'):
                current_pos = next_tag_end + 1
                break
            
            if next_tag_content.startswith('/'):
                # Other closing tag - shouldn't happen in well-formed HTML
                current_pos = next_tag_end + 1
            else:
                # Parse child element recursively
                child, current_pos = self._parse_element(html, next_tag_start)
                if child:
                    element.children.append(child)
        
        return element, current_pos
    
    def _extract_attributes(self, tag_content: str) -> Dict[str, str]:
        """
        Extract attributes from a tag's content.
        
        Args:
            tag_content: The content of the tag (between < and >).
        
        Returns:
            Dictionary of attribute name-value pairs.
        """
        attributes = {}
        # Pattern to match attributes
        attr_pattern = r'(\w+)\s*=\s*["\']([^"\']*)["\']'
        matches = re.findall(attr_pattern, tag_content)
        
        for attr_name, attr_value in matches:
            attributes[attr_name.lower()] = attr_value
        
        return attributes
