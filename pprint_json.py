import json
import argparse
import os.path
import codecs
import sys


def load_data(filepath):
    with codecs.open(filepath, "r", "utf-8") as json_file:
        json_content = json_file.read()
        json_file.close()
        try:
            return json.loads(json_content)
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


def get_json_path():
    parser = argparse.ArgumentParser()
    help = "custom json file path"
    parser.add_argument("-f", "--file", dest="json_path", help="help")
    args = parser.parse_args()
    json_path = args.json_path
    if json_path is None:
        json_path = "raw.json"
    return json_path


if __name__ == '__main__':
    json_path = get_json_path()
    if not os.path.isfile(json_path):
        print("error: can't find file {}".format(json_path))
        sys.exit()
    parsed_json = load_data(json_path)
    if not parsed_json:
        print("file content is not valid json")
        sys.exit()
    pretty_print_json(parsed_json)
