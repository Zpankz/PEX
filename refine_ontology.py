import os
import yaml
from pathlib import Path


def load_front_matter(path):
    """Return YAML front matter and remainder of file."""
    text = path.read_text(encoding='utf-8')
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            fm, rest = parts[1], parts[2]
            try:
                data = yaml.safe_load(fm) or {}
            except yaml.YAMLError:
                data = {}
                rest = text
            return data, rest.lstrip('\n')
    return {}, text


def dump_front_matter(data, content):
    fm = yaml.dump(data, sort_keys=False)
    return f"---\n{fm}---\n{content}"


def refine_properties(data):
    """Ensure ontology fields exist with default types."""
    data.setdefault('principles', ['Parsimony', 'Recursion', 'Structure-Dynamics'])
    foundations = data.setdefault('foundations', {})
    foundations.setdefault('dimension', {'spatial': None, 'temporal': None})
    foundations.setdefault('perspective', None)
    foundations.setdefault('operators', [])
    structures = data.setdefault('structures', {})
    structures.setdefault('entities', [])
    structures.setdefault('edges', [])
    structures.setdefault('clusters', [])
    data.setdefault('interactions', {})
    data.setdefault('processes', {})
    data.setdefault('frameworks', [])
    return data


def process_file(path):
    data, content = load_front_matter(path)
    new_data = refine_properties(data)
    path.write_text(dump_front_matter(new_data, content), encoding='utf-8')


if __name__ == "__main__":
    for root, _, files in os.walk('.'):
        for f in files:
            if f.endswith('.md'):
                p = Path(root) / f
                process_file(p)
