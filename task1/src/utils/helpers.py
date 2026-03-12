from typing import List, Dict, Any
import requests
import pandas as pd


def fetch_posts(api_url: str) -> List[Dict[str, Any]]:
    """
    Fetch posts from the provided API endpoint.
    
    Args:
        api_url: URL of the API endpoint to fetch posts from
        
    Returns:
        List of post dictionaries from the API response
        
    Raises:
        Exception: If the API request fails
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts from {api_url}: {str(e)}")
        raise


def print_posts(posts: List[Dict[str, Any]]) -> None:
    """
    Print all posts in a formatted manner.
    
    Args:
        posts: List of post dictionaries to print
    """
    separator = "=" * 80
    for post in posts:
        print(f"UserId:\t\t{post['userId']}")
        print(f"Post ID:\t\t{post['id']}")
        print(f"Title:\t\t{post['title']}")
        body_formatted = ' '.join(str(post['body']).strip().split('\n'))
        print(f"Body:\t\t{body_formatted}")
        print(separator)


def create_dataframe(data: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Convert list of post dictionaries to a pandas DataFrame.
    
    Args:
        data: List of post dictionaries
        
    Returns:
        DataFrame with post data
    """
    return pd.DataFrame(data)