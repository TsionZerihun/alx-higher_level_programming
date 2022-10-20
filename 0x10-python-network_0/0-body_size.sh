#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI GET "$1" | grep -i "content-length" | cut -d " " -f2
