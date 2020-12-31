import json
import sys

def get_all():
    with open('./settings.json') as f:
        return json.loads(f.read())


def get_value(key):
    return get_all().get(key)


if __name__ == '__main__':
    key = sys.argv[1]
    print(get_value(key))