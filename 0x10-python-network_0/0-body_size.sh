#!/bin/bash
# Script that takes in, sends a request and displays the response of URL.
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
