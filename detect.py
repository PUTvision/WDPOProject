import json
from pathlib import Path
from typing import Dict

import click
import cv2
from tqdm import tqdm


def detect(img_path: str) -> Dict[str, int]:
    """Object detection function, according to the project description, to implement.

    Parameters
    ----------
    img_path : str
        Path to processed image.

    Returns
    -------
    Dict[str, int]
        A dictionary with the number of each object.
    """
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    #TODO: Implement detection method.
    
    aspen = 0
    birch = 0
    hazel = 0
    maple = 0
    oak = 0

    return {'aspen': aspen, 'birch': birch, 'hazel': hazel, 'maple': maple, 'oak': oak}


@click.command()
@click.option('-p', '--data_path', help='Path to data directory', type=click.Path(exists=True, file_okay=False, path_type=Path), required=True)
@click.option('-o', '--output_file_path', help='Path to output file', type=click.Path(dir_okay=False, path_type=Path), required=True)
def main(data_path: Path, output_file_path: Path):
    img_list = data_path.glob('*.jpg')

    results = {}

    for img_path in tqdm(sorted(img_list)):
        leaves = detect(str(img_path))
        results[img_path.name] = leaves

    with open(output_file_path, 'w') as ofp:
        json.dump(results, ofp)


if __name__ == '__main__':
    main()
