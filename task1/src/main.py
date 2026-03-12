"""
Task 1 - Python Requests Analysis
Fetches posts from JSONPlaceholder API and performs data analysis.

Tasks:
a) Fetch data from https://jsonplaceholder.typicode.com/posts
b) Fetch all posts and print them
c) Count distinct number of users
d) Identify user with highest number of posts
e) Calculate average word length of post titles
"""

from typing import Dict, Any
import pandas as pd

from config import settings
from utils import fetch_posts, print_posts, create_dataframe


# ============================================================================
# ANALYSIS FUNCTIONS
# ============================================================================


def analyze_distinct_users(df: pd.DataFrame) -> int:
    """
    Count distinct number of users in the dataset.
    
    Args:
        df: DataFrame containing post data
        
    Returns:
        Number of distinct users
    """
    return df["userId"].nunique()


def analyze_user_post_counts(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Identify user with highest number of posts.
    
    Args:
        df: DataFrame containing post data
        
    Returns:
        Dictionary with user_id, post_count, and full dataframe of user counts
    """
    user_counts = (
        df.groupby("userId")
        .size()
        .reset_index(name="post_count")
        .sort_values("post_count", ascending=False)
    )
    
    top_user = user_counts.iloc[0]
    
    return {
        "user_id": int(top_user["userId"]),
        "post_count": int(top_user["post_count"]),
        "all_counts": user_counts
    }


def analyze_average_word_length(df: pd.DataFrame) -> float:
    """
    Calculate average word length across all post titles.
    
    Args:
        df: DataFrame containing post data
        
    Returns:
        Average word length of all post titles
    """
    # Split titles into words and calculate average word length per title
    title_word_lengths = df["title"].str.split().apply(
        lambda words: sum(len(word) for word in words) / len(words) if words else 0
    )
    
    return title_word_lengths.mean()


# ============================================================================
# OUTPUT FORMATTING FUNCTIONS
# ============================================================================


def print_section(section_id: str, title: str) -> None:
    """Print formatted section header."""
    print("\n" + "=" * 80)
    print(f"{section_id}) {title}")
    print("=" * 80)


def main() -> None:
    """Main execution function."""
    
    # Fetch data from API
    print("Fetching posts from API...")
    posts_data = fetch_posts(settings.USER_POSTS)
    print(f"Successfully fetched {len(posts_data)} posts.\n")
    
    # b) Print all posts
    print_section("b", "FETCHING AND PRINTING ALL POSTS")
    print_posts(posts_data)
    
    # Create DataFrame for analysis
    df = create_dataframe(posts_data)
    
    # c) Count distinct users
    print_section("c", "DISTINCT NUMBER OF USERS")
    unique_users = analyze_distinct_users(df)
    print(f"Total distinct users: {unique_users}\n")
    
    # d) User with highest number of posts
    print_section("d", "USER WITH HIGHEST NUMBER OF POSTS")
    user_stats = analyze_user_post_counts(df)
    print(user_stats["all_counts"].to_string(index=False))
    print(
        f"\n➤ User {user_stats['user_id']} has the highest number "
        f"of posts: {user_stats['post_count']} posts\n"
    )
    
    # e) Average word length of post titles
    print_section("e", "AVERAGE WORD LENGTH OF POST TITLES")
    avg_word_length = analyze_average_word_length(df)
    print(f"Average word length in post titles: {avg_word_length:.2f} characters\n")


if __name__ == "__main__":
    main()