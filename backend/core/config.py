from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASE_URL = f"sqlite:///{BASE_DIR / 'atlas.db'}"

APP_NAME = "Atlas d'Atthil"
VERSION = "0.1.0"