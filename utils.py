import json

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
def save_txt(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

def load_txt(filename):
    with open(filename, 'r') as f:
        return f.read()