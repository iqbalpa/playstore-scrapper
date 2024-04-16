import json

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)

def load_txt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()