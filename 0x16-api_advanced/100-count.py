#!/usr/bin/python3
"""
This module is for task 3, which involves querying the Reddit API and
returning the count of words in word_list in the titles of all the hot posts
of the subreddit.
"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API and returns the count of words in word_list in
    the titles of all the hot posts of the subreddit.

    :param subreddit: The name of the subreddit to query.
    :param word_list: A list of words to count in post titles.
    :param word_count: A dictionary to store the word counts.
    :param after: The "after" parameter for pagination.
    :return: None if an error occurs
    """
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code != 200:
        return None

    info = sub_info.json()

    hot_l = [child.get("data").get("title")
             for child in info
             .get("data")
             .get("children")]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
