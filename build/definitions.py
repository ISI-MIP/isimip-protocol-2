import json
import os
import subprocess
from pathlib import Path


def main():
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()

    directory = Path('definitions')
    definitions = {}
    for file_name in os.listdir(directory):
        file_path = directory / file_name

        with open(file_path) as f:
            definitions[file_path.stem] = json.loads(f.read())

    simulation_rounds = [definition['specifier'] for definition in definitions['simulation_round']]
    products = [definition['specifier'] for definition in definitions['product']]
    sectors = [definition['specifier'] for definition in definitions['sector']]

    for simulation_round in simulation_rounds:
        for product in products:
            for sector in sectors:
                output_path = Path('output').joinpath('definitions') \
                                            .joinpath(simulation_round).joinpath(product).joinpath(sector) \
                                            .with_suffix('.json')
                output_path.parent.mkdir(parents=True, exist_ok=True)

                output_definitions = {
                    'commit': commit,
                }
                for definition_name, rows in definitions.items():
                    # filter definitions for simulation_round, product, sector
                    output_definitions[definition_name] = []
                    for row in rows:
                        if 'simulation_rounds' not in row or simulation_round in row['simulation_rounds']:
                            if 'products' not in row or product in row['products']:
                                if 'sectors' not in row or sector in row['sectors']:
                                    output_definitions[definition_name].append(row)

                with open(output_path, 'w') as f:
                    f.write(json.dumps(output_definitions, indent=2))


if __name__ == "__main__":
    main()