#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request as request

if __name__ ==  "__main__":
    from urllib import request
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as r:
        data = r.read()
        print("Body respone:")
        print("\t - type: {}".format(type(data)))
        print("\t - content: {}".format(data))
        print("\t - utf8 content: {}".format(data.decode("UTF-8")))
