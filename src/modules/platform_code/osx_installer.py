import json

def osx_init(config_json):
    with open(config_json) as f:
        config_dict = json.loads(f.read())

    print(config_dict)