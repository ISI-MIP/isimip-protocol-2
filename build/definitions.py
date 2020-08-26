import json
import os
from pathlib import Path


def main():
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
                output_path = Path('output') / 'definitions' / simulation_round / product / sector
                output_path.mkdir(parents=True, exist_ok=True)

                with open(output_path / 'index.json', 'w') as f:
                    f.write(json.dumps(list(definitions.keys()), indent=2))

                for definition_name, rows in definitions.items():
                    # filter definitions for simulation_round, product, sector
                    definition = []
                    for row in rows:
                        if 'simulation_rounds' not in row or simulation_round in row['simulation_rounds']:
                            if 'products' not in row or product in row['products']:
                                if 'sectors' not in row or sector in row['sectors']:
                                    definition.append(row)

                    with open(output_path.joinpath(definition_name).with_suffix('.json'), 'w') as f:
                        f.write(json.dumps(definition, indent=2))


if __name__ == "__main__":
    main()
