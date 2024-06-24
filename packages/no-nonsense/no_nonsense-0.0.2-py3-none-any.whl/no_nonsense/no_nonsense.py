import argparse
import os
from typing import Any

from pathlib import Path


from ruamel.yaml import YAML
from wheezy.template import Engine, FileLoader, CoreExtension, CodeExtension


def generate_site(config: dict[str, Any], input_file: Path, output_dir: Path) -> None:
    engine = Engine(
        loader=FileLoader([str(input_file.parent)]),
        extensions=[CoreExtension(), CodeExtension()]
    )

    for output_name, data in config['templates'].items():
        template = engine.get_template(data['input'])

        file = Path(f'{output_dir}/{output_name}')
        # output_name may be abc/def. In this case, we need to make sure abc exists.
        # Otherwise, open throws an error
        os.makedirs(file.parent, exist_ok=True)

        with open(file, 'w+') as fp:
            fp.write(template.render({'config': config, 'this': data}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='No Nonsense',
        description='Static Site Generator that uses wheezy.template as template engine and YAML for configuration',
        epilog='Get stuff done. Happy Hacking :)')

    parser.add_argument('-f', help='YAML file containing config', default='nn.yaml', metavar='file', dest='file')
    parser.add_argument('-o', help='Output directory. By default it is <directory containing yaml file>/public. It will delete the ', metavar='out_dir', dest='out_dir')
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
    args = parser.parse_args()

    input_file = Path(args.file)

    try:
        config = YAML(typ='safe').load(input_file)
        if type(config) is not dict:
            print(f'File: {input_file} is not a valid config')
            exit(2)

        generate_site(config, input_file, Path(args.out_dir if args.out_dir is not None else f'{input_file.parent}/public'))
    except FileNotFoundError as e:
        print(f'File: {e.filename} not found')
        exit(1)
