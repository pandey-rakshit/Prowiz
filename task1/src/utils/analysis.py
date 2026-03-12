from typing import Tuple
import pandas as pd


def count_distinct_users(df: pd.DataFrame) -> int:
    """
    Count the number of distinct users in the dataset.
    
    Args:
        df: DataFrame containing post data with 'userId' column
        
    Returns:
        Number of distinct users
    """
    return df["userId"].nunique()


def get_user_post_counts(df: pd.DataFrame) -> Tuple[pd.DataFrame, int, int]:
    """
    Get the count of posts per user and identify the user with most posts.
    
    Args:
        df: DataFrame containing post data with 'userId' column
        
    Returns:
        Tuple containing:
            - DataFrame with userId and post_count columns sorted by count
            - User ID with highest number of posts
            - Maximum number of posts
    """
    user_post_counts = (
        df.groupby(by="userId")
        .size()
        .reset_index(name="post_count")
        .sort_values("post_count", ascending=False)
    )
    
    max_user_row = user_post_counts.iloc[0]
    max_user_id = int(max_user_row["userId"])
    max_post_count = int(max_user_row["post_count"])
    
    return user_post_counts, max_user_id, max_post_count


def calculate_avg_word_length(df: pd.DataFrame) -> float:
    """
    Calculate the average word length across all post titles.
    
    Args:
        df: DataFrame containing post data with 'title' column
        
    Returns:
        Average word length across all titles
    """
    # Split titles into words
    df_copy = df.copy()
    df_copy['title_words'] = df_copy['title'].str.split()
    
    # Calculate word lengths for each title
    df_copy['word_lengths'] = df_copy['title_words'].apply(
        lambda words: [len(word) for word in words]
    )
    
    # Calculate average word length per title
    df_copy['avg_word_length'] = df_copy['word_lengths'].apply(
        lambda lengths: sum(lengths) / len(lengths) if lengths else 0
    )
    
    # Return overall average
    return df_copy['avg_word_length'].mean()
