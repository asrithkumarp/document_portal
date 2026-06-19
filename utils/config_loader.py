import yaml

def load_config(congig_path: str="config\config.yaml")->dict:
    with open(congig_path,"r") as file:
        config=yaml.safe_load(file)
    return config

load_config()