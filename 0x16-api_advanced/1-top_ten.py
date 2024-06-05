#!/usr/bin/python3
"""
1-top_ten module
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit
    If the subreddit is invalid, prints None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent'}
    params = {'limit': 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                for post in posts:
                    print(post['data']['title'])
            except ValueError:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
