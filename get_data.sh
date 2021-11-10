#!/bin/sh

wget https://storage.googleapis.com/generall-shared-data/startups_demo.json
mv startups_demo.json data/startups.json
rm startups_demo.json
