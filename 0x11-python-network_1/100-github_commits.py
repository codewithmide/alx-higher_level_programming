#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    rep = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, rep)
    request = requests.get(url)
    count = 0
    for i in request.json():
        print(i.get('sha') + ": " + i.get('commit').get('author').get('name'))
        count += 1
        if count == 10:
            break
