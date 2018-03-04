import json
import argparse
import os.path
import codecs
import sys


def load_data(filepath):
    with codecs.open(filepath, "r", "utf-8") as json_file:
        json_content = json_file.read()
        try:
            return json.loads(json_content)
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(parsed_json):
    print(json.dumps(parsed_json, indent=4, sort_keys=True,
                     ensure_ascii=False))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        dest="json_path",
        help="custom json file path",
        default="raw.json"
    )
    return parser.parse_args()


if __name__ == "__main__":
    json_path = get_args().json_path
    if not os.path.isfile(json_path):
        sys.exit("error: can't find file {}".format(json_path))
    parsed_json = load_data(json_path)
    if not parsed_json:
        sys.exit("file content is not valid json")
    pretty_print_json(parsed_json)
