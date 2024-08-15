#!/usr/bin/python3
"""
Print top 10 posts on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries and prints the titles of to ten posts of a
        given Reddit subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"user-agent": "request"}

    params = {"limit": 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    result = response.json().get("data").get("children")

    top_10_posts = "\n".join(post.get("data").get("title") for post in result)

    print(top_10_posts)
