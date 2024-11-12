#!/usr/bin/python3
"""
This module contains a function to query the Reddit API and
print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the first 10 hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the first 10 hot posts or None if the subreddit is invalid.
    """
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}

    # Prevent following redirects
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            if posts:
                for post in posts[:10]:
                    print(post['data'].get('title'))
            else:
                print(None)
        except (KeyError, ValueError):
            # If there's an issue with accessing JSON or structure is unexpected
            print(None)
    else:
        print(None)

