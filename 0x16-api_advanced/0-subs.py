#!/usr/bin/python3
"""
This module is for task 0, which involves querying the Reddit API
and returning the number of subscribers to a subreddit.
"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    to the subreddit.

    :param subreddit: The name of the subreddit to query.
    :return: The number of subscribers or 0 if an error occurs.
    """
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
