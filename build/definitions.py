import json
import os
import shutil
from pathlib import Path


def main():
    directory = Path('definitions')
    definitions = []
    for file_name in os.listdir(directory):
        source = directory / file_name
        target = Path('output') / source

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, target)

        definitions.append(file_name)

    with open(Path('output') / directory / 'index.json', 'w') as f:
        f.write(json.dumps(definitions, indent=2))


if __name__ == "__main__":
    main()
