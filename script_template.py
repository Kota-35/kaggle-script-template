import gzip
import base64
import subprocess
from pathlib import Path
from typing import Dict


# this is base64 encoded source code
file_data: Dict = {file_data}


for path, encoded in file_data.items():
    print(path)
    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    path.write_bytes(gzip.decompress(base64.b64decode(encoded)))


def run(command):
    result = subprocess.run(command, shell=True, check=True, text=True)
    return result


run('python setup.py develop --install-dir /kaggle/working')
run('python easy_gold/main.py')
