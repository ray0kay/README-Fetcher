# README Fetcher
# Created by ray0kay
# GitHub: https://github.com/ray0kay

import argparse
import requests
import time
import sys
import random
from bs4 import BeautifulSoup as bs

parser = argparse.ArgumentParser(
    description="Fetch the README.md file from a GitHub repository."
)

parser.add_argument(
    "url", type=str, help="The URL of the GitHub repository README file to fetch."
)

args = parser.parse_args()

url = args.url

if url.endswith("/"):
    url = url[:-1]

response = requests.get(url)

soup = bs(response.content, "html.parser")

text = soup.find("article", class_="markdown-body entry-content container-lg")
has_image = args.has_image

if text is None:
    print("No text found in the provided URL.")
    time.sleep(2)
    sys.exit(1)
else:
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(
            '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <style>body {font-family: "Trebuchet MS", sans-serif}</style>
        <title>README Fetcher Output</title>
    </head>
    <body>
    <h1>README Fetcher Output</h1>
''')
        file.write(text.prettify())

print('\nThe results are available in output.html!\n')

time.sleep(1.5)
sys.exit(0)
