#!/usr/bin/python3
"""
    Query a list of all hot post in a given Reddit subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
        Returns List of titles in a hot post in a given subredit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"user-agent": "request"}

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    results = response.json().get("data")

    after = results.get("after")

    count += results.get("dist")

    for child in reults.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
