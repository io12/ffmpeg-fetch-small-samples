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

    if path == '.':
        continue

    print(path)

    # Check if file is <5M
    r = requests.get(BASE_URL + path, stream=True)
    if int(r.headers['content-length']) <= 5 * 10 ** 6:

        # Download file
        basename = os.path.basename(path)
        save = f'{OUT_PATH}/{basename}'
        with open(save, 'wb') as f:
            f.write(r.content)
