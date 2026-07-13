import json
from pathlib import Path


class JsonImporter:

    @staticmethod
    def load(path: str):

        with open(Path(path), encoding="utf-8") as f:
            return json.load(f)