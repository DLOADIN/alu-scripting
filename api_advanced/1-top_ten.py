#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints titles of the top 10 hot posts from a given subreddit. If invalid, print None."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        response = requests.get(subreddit_url, headers=headers, timeout=10)
        if response.status_code == 200:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])
            
            if len(posts) == 0:
                print("None")
                return
            
            for post in posts:
                print(post.get('data', {}).get('title', 'None'))
            return "OK"
        else:
            print("None")
            return "None"
    except requests.exceptions.RequestException:
        print("None")
        return "None"
