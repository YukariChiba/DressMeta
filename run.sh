#!/bin/bash

git submodule foreach git pull

mkdir -p data
mkdir -p tmp

tree -J -I '*.md|*.yml' dress | jq '.[0]["contents"]' > tmp/tmp.json

python3 process.py
