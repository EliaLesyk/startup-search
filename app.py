import argparse
import csv
import os
import sys

from jina import DocumentArray
from jina.types.document.generators import from_csv

from config import data_path
from flows import search_flow, index_flow
from helpers import download_json_to_csv, log


# boolean args: https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse/36031646
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_args():
    # Command line arguments definitions
    parser = argparse.ArgumentParser()
    parser.add_argument('--index',
        dest='index',
        default=False,
        action='store_true',
        help="index the available documents"
    )
    parser.add_argument("--n", type=int, default=0, help="when `--index` is used, specifies the number of documnts to index (0 indexes the full dataset)")

    return parser.parse_args()


def index(n):
    if not os.path.exists(data_path):
        log("Downloading data...")
        download_json_to_csv()

    csv.field_size_limit(sys.maxsize)

    with open(data_path) as data_file:
        docs_generator = from_csv(
                data_file,
                #field_resolver={"name": "name"},
        )
        startups = DocumentArray(docs_generator)

        for startup in startups:
            startup.text = startup.tags["name"] + "[SEP]" + startup.tags["description"]

    if n != 0:
        startups = startups[:n]

    log(f"Loaded {len(startups)} startups from {data_path}.")

    log("Building index...")
    indexer = index_flow()
    with indexer:
        indexer.index(startups, request_size=32)


args = get_args()

if args.index:
    index(args.n)

# running the search/finetuning flow as a service
flow = search_flow()
flow.expose_endpoint('/finetune', summary='Finetune documents.', tags=['Finetuning'])

with flow:
    log("Ready for searching.")
    flow.block()
