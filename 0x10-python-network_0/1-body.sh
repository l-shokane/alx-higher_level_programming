#!/bin/bash
# Script that takes in, sends a request and displays the response of a URL.
curl -sX GET $1 -L
