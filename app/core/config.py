from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATABASE_URL = f"sqlite:///{PROJECT_ROOT / 'atlas.db'}"

APP_NAME = "Atlas d'Atthil"

VERSION = "0.1.0"