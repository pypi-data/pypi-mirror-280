from pathlib import Path


def findfile():
    basedir = Path(__file__).resolve().parent.parent

    py_files = basedir.glob(f'*/*.py')
    return [file.name for file in py_files]


print(*findfile())
