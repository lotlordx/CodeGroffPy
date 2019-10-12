from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feeds = feedparser.parse(FEED_URL).entries
    result = []

    # return Game(title=)

    for item in feeds:
        data = Game(title=item.title, link=item.link)
        result.append(data)
    return result

print(get_games())