# ffmpeg-fetch-small-samples

Script to fetch small files from https://samples.ffmpeg.org/

## Usage

Run `./fetch.py` and all files less than one megabyte will be downloaded from the FFmpeg samples collection.

## Purpose

This can be used to ease coverage-guided fuzzing of FFmpeg. The samples can be used as an initial corpus for the fuzzer. However, many of the samples are large, which make them unsuitable for fuzzing.
