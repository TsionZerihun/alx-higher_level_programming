#!/usr/bin/python3
# Script that fetches https://alx-intranet.hbtn.io/status

import urllib.request
url =  "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as r:
     data = r.read()
     data = data.decode("UTF-8")
     print(data)


