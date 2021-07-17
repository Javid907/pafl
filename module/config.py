import yaml

with open("/etc/pafl/template.yaml", "r") as config:
    try:
        config_file = yaml.safe_load(config)
    except yaml.YAMLError as exc:
        print(exc)


def get_config(my_config):
    return config_file[my_config]
