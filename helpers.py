import csv
import json
import os
from urllib.request import urlretrieve

from config import print_logs, json_data_url, data_path, json_path


def download_json_to_csv():
    if not os.path.isdir('data/'):
        os.makedirs('data/')
    if not os.path.exists(data_path):
        if not os.path.exists(json_path):
            urlretrieve(json_data_url, json_path)
        # open json file
        data = open(json_path, 'r').readlines()
        startups = []
        for line in data:
            startups.append(json.loads(line))
        # create csv file
        data_file = open(data_path, 'w', newline='')
        csv_writer = csv.writer(data_file)
        count = 0
        for startup in startups:
            if count == 0:
                header = startup.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(startup.values())
        data_file.close()


def log(message):
    if print_logs:
        print(message)
