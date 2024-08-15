#!/usr/bin/python3
"""
Counts keywords of all hot post of a Reddit subreddit.
"""
import requests
import sys


def count_words(subreddit, word_list, after=None, count={}):
    """
    Function that queries a Reddit API, parses all hot post titles,
       and prints a sorted count of keywords.
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"user-agent": "request"}

    params = {"limit": 100}

    if after:
        params['after'] = after

    response = requests.get(url,
                            headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    main_info = response.json()

    info = main_info.get("data")

    sub_info = info.get("children")

    for post in sub_info:
        title = post.get("data", {}).get("title").lower()

        for word in word_list:
            if word.lower() in title:
                count[word] = count.get(word, 0) + title.count(word.lower())
    after = main_info.get("data", {}).get("after")
    if after:
        count_words(subreddit, word_list, after, count)
    else:
        sorted_count = sorted(count.items(),
                              key=lambda x: (-x[1], x[0].lower()))

        for word, num in sorted_count:
            print("{}: {}".format(word.lower(), num))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javaScript'"
              .format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
