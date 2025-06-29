import os
import yaml
from collections import defaultdict

def extract_yaml_from_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) > 2:
            try:
                return yaml.safe_load(parts[1])
            except yaml.YAMLError:
                return None
    return None

def scan_repo(root_dir):
    schema = defaultdict(set)
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if name.endswith('.md'):
                path = os.path.join(root, name)
                data = extract_yaml_from_file(path)
                if isinstance(data, dict):
                    for key, value in data.items():
                        schema[key].add(type(value).__name__)
    return {k: sorted(list(v)) for k, v in schema.items()}

if __name__ == '__main__':
    schema = scan_repo('.')
    with open('schema.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(schema, f, sort_keys=False)
    print('Schema written to schema.yaml')
