# README Fetcher
# Created by ray0kay
# GitHub: https://github.com/ray0kay

import argparse
import requests
import time
import sys
import random
from bs4 import BeautifulSoup as bs

def str2bool(v):
    if v.lower() == 'true':
        return True
    elif v.lower() == 'false':
        return False

def send_message():
    messages = [
        'Fetching data...',
        'Going to the supermarket...',
        'Watching Netflix...',
        'Eating seafood...',
        'Taking a nap...'
    ]

    return random.choice(messages)

parser = argparse.ArgumentParser(
    description="Fetch the README.md file from a GitHub repository."
)

parser.add_argument(
    "url", type=str, help="The URL of the GitHub repository README file to fetch."
)

parser.add_argument(
    "has_image",
    type=str2bool,
    help="True if the README.md file has an image(s), False otherwise.",
    nargs="?",
    default=False,
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
        <p>
'''
        )
    print(f'\n{send_message()}\n')
    print("Text found.")

    with open("output.html", "a", encoding="utf-8") as file:
        file.write(f'{text.get_text()}</p>\n')
    time.sleep(2)

if has_image is True:
    print(f'\n{send_message()}\n')
    time.sleep(2)
    image = text.find("img")
    if image is not None:
        print("Image found.")

        with open("output.html", "a") as file:
            file.write(f'<img src="{image["src"]}" alt="Image" style="max-width: 100%; height: auto;">\n')
        
        time.sleep(2)
    else:
        print("No image found.")
        time.sleep(2)
        sys.exit(1)
else:
    with open("output.html", "a", encoding="utf-8") as file:
        file.write('</body>\n</html>')

print('\nThe results are available in output.html!\n')

time.sleep(1.5)
sys.exit(0)