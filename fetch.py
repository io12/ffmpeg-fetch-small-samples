#!/usr/bin/env python3

import os
import requests

BASE_URL = 'https://samples.ffmpeg.org/'
OUT_PATH = 'out'

# Create output directory
os.mkdir(OUT_PATH)

# Iterate over paths of sample files
r = requests.get(BASE_URL + 'allsamples.txt')
for path in r.text.splitlines():

    basename = os.path.basename(path)

    if basename == '.' or '.' not in basename:
        continue

    print(path)

    # Get header
    url = BASE_URL + path
    r = requests.head(url)

    # Get file size
    try:
        size = int(r.headers['content-length'])
    except KeyError:
        continue

    # Check if file is <5M
    if size <= 5 * 10 ** 6:

        # Download file
        r = requests.get(url)
        save = f'{OUT_PATH}/{basename}'
        with open(save, 'wb') as f:
            f.write(r.content)
