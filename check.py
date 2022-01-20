import json
import urllib.error
import urllib.request
from http.client import HTTPResponse
from io import BytesIO
from pathlib import Path
from typing import Dict, Any
from zipfile import ZipFile, ZIP_DEFLATED

URL = 'https://wdpo.dpieczynski.pl'


def main():
    student_id = 000000  # Tutaj należy wpisać swój numer indeksu

    data = BytesIO()
    with ZipFile(data, 'w', ZIP_DEFLATED) as zip_file:
        base_path = Path.cwd()
        for file in base_path.rglob('*'):
            zip_file.write(file, file.relative_to(base_path))

    data.seek(0)

    try:
        response: HTTPResponse = urllib.request.urlopen(f'{URL}/{student_id}', data.read())
        response: Dict[str, Any] = json.loads(response.read())
        print(response)
    except urllib.error.HTTPError as e:
        response: Dict[str, Any] = json.loads(e.read())
        print('ERROR')
        print(response['data'])
        if response['logs']:
            print()
            print('LOGS:')
            print(response['logs'])


if __name__ == '__main__':
    main()
