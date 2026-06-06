import json


def load_styles(config_path="configs/styles.json"):
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    styles = load_styles()
    print(styles.keys())