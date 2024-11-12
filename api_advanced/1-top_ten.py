#!/usr/bin/python3

"""
Displays the titles of 10 hot posts listed for a subreddit
"""
def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
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
            # If there's an issue with accessing JSON or it doesn't have expected structure
            print(None)
    else:
        print(None)
