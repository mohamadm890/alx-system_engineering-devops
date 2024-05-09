#!/usr/bin/python3
"""AdvancedAPI"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of suscriber for a given subreddit"""
    base_url = 'https://www.reddit.com'
    query = 'r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:hbtn.advanced.api (by /u/koeusiss)"
    }
    req = requests.get(
        url='{}/{}'.format(base_url, query),
        headers=headers,
        allow_redirects=False
    )
    if req.status_code == 404:
        return 0
    res = req.json()
    return res.get('data').get('subscribers')

if __name__ == '__main__':
    number_of_subscribers(subreddit)
