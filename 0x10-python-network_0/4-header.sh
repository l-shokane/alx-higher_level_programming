#!/bin/bash
# Script that sends a GET request and displays the response.
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
