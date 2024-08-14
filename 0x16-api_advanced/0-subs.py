#!/usr/bin/python3
"""
Uses Reddit API to print the number of subreddit subscribers
"""
import requests

def number_of_subscribers(subreddit):
	"""
	Print the number of subscribers of a a subreddit
	"""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {"user-agent": "linux: 0x16.advanced: v1 0.0 (by /u/bdov_)"}
	response = requests.get(url, headers=headers, allow_redirects=False)
	
	if response.status_code != 200:
		return 0

	result = response.json().get("data")
	num_subs = result.get("subscribers")

	return num_subs
