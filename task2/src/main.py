from typing import Dict

from soup_parser import BeautifulSoupParser
from html_parser import RecursiveHTMLParser


# HTML content to parse
HTML_CONTENT = """<html><head><title>The Dormouse's story</title></head><body> 
<p class="title"><b>The Dormouse's story</b></p> 
<p class="story">Once upon a time there were three little sisters; and their 
names were 
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p> 
<p class="story">...</p> 
</body></html>"""


def print_section(title: str, data: any, is_list: bool = True) -> None:
    """Pretty print a section of results."""
    print(f"  {title}")
    print(f"{'='*70}")
    
    if is_list:
        for i, item in enumerate(data, 1):
            print(f"  {i}. {item}")
    else:
        for key, value in data.items():
            print(f"  {key}: {value}")
    
    print()


def parse_with_beautifulsoup() -> Dict[str, any]:
    """Use BeautifulSoup to extract data."""
    print("  BeautifulSoup Parser")
    print("="*70)
    
    parser = BeautifulSoupParser(HTML_CONTENT)
    results = parser.parse()
    
    print_section("HREF Links", results["href_links"])
    print_section("Classes in <a> tags", results["anchor_classes"])
    
    return results


def parse_with_recursive() -> Dict[str, any]:
    """Use our custom recursive parser (no external deps)."""
    print("  Recursive Parser (No External Dependencies)")
    print("="*70)
    
    parser = RecursiveHTMLParser(HTML_CONTENT)
    results = parser.parse()
    
    print_section("HREF Links", results["href_links"])
    print_section("Classes in <a> tags", results["anchor_classes"])
    
    return results


def compare_results(bs_results: Dict[str, any], 
                   rec_results: Dict[str, any]) -> None:
    """Check if both parsers got the same results."""
    print("\n" + "="*70)
    print("  Results Comparison")
    print("="*70)
    
    # check if hrefs match
    bs_hrefs = set(bs_results["href_links"])
    rec_hrefs = set(rec_results["href_links"])
    match_hrefs = bs_hrefs == rec_hrefs
    print(f"\n  hrefs match: {match_hrefs}")
    
    # check classes too
    bs_classes = set(bs_results["anchor_classes"])
    rec_classes = set(rec_results["anchor_classes"])
    match_classes = bs_classes == rec_classes
    print(f"  classes match: {match_classes}")
    
    print()


def main() -> None:
    """Run both parsers and compare results."""
    
    print("\n")
    print("="*70)
    print("  HTML Parser".center(70))
    print("="*70)
    
    bs_results = None
    rec_results = None
    
    # Try BeautifulSoup
    try:
        bs_results = parse_with_beautifulsoup()
    except ImportError:
        print("\nBeautifulSoup not installed. Run: pip install beautifulsoup4\n")

    
    rec_results = parse_with_recursive()
    if bs_results and rec_results:
        compare_results(bs_results, rec_results)
    print("="*70)
    print("Done")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()