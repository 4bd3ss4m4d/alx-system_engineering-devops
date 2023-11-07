#!/usr/bin/python3
"""
This module is for task 2, which involves querying the Reddit API and
returning all hot posts of a subreddit.
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit API and returns all hot posts of the subreddit.

    :param subreddit: The name of the subreddit to query.
    :param hot_list: A list to store the post titles.
    :param count: The count parameter for pagination.
    :param after: The "after" parameter for pagination.
    :return: A list containing the post titles or None if an error occurs.
    """
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in sub_info.json()
                        .get("data")
                        .get("children")]

    info = sub_info.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
