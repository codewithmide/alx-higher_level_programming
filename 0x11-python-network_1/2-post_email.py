#!/usr/bin/python3
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as request:
        response = request.read()
    print(response.decode("utf-8"))
