#!/usr/bin/python3
"""0-subs module"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API

    Returns:
        the number of subscribers for a given subreddit,
        0 if an invalid subreddit is given
    """
    URL = 'https://www.reddit.com/r/'
    res = requests.get('{}{}/about.json'.
                       format(URL, subreddit),
                       headers={'User-Agent': 'ALX-User-Agent'},
                       allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')
