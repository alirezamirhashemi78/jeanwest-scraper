import json
import os

DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_json(file):
    path = os.path.join(DATA_DIR, file)
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_json(data, file):
    path = os.path.join(DATA_DIR, file)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def save_product(data):
    splited_path = os.getcwd().split('/')
    filename = splited_path[-2] + "_" + splited_path[-1] + ".json"

    loaded = load_json(filename)
    if not loaded:
        loaded = {"products": []}

    loaded["products"].append(data)
    save_json(loaded, filename)
    print(f"[+] Saved product data to '{filename}'")

def is_id_exist(product_id, ids_file="ids.json"):
    loaded = load_json(ids_file)
    if not loaded:
        loaded = {"ids": []}

    if product_id in loaded["ids"]:
        print(f"[!] Product ID <{product_id}> already processed. Skipping.")
        return True

    loaded["ids"].append(product_id)
    save_json(loaded, ids_file)
    print(f"[+] Recorded new product ID <{product_id}>")
    return False
