#!/usr/bin/python3
"""
Module to query Reddit API and get top 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints the titles of first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit: string - the name of the subreddit to query

    Returns:
        None if subreddit is invalid,
        Otherwise prints the titles of the first 10 hot posts
    """
    # Reddit API URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid too many requests error
    headers = {
        'User-Agent': 'linux:0.1:v1.0 (by /u/your_username)'
    }

    # Parameters to limit number of posts and avoid redirects
    params = {
        'limit': 10
    }

    try:
        # Make GET request to Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check if subreddit exists
        if response.status_code == 404:
            print(None)
            return
        # Check if other errors occurred
        if response.status_code != 200:
            print(None)
            return

        # Parse response JSON
        results = response.json()
        posts = results.get('data', {}).get('children', [])

        # Print first 10 post titles
        for post in posts:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)
