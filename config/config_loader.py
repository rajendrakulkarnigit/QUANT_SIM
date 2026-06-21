import yaml

def load_config(path="config/config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def load_credentials(path="config/credentials.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)
