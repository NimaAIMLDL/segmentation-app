"""Configurations for sptf-app"""
# ------------------------------ Import Libraries -----------------------------
from pathlib import Path  # Object-oriented filesystem paths
# ----------------------------- Config App Paths ------------------------------
APP_PATH = (Path(__file__).resolve())
data_path = ((APP_PATH).resolve().parents[2] / './data/').resolve()
cwd = ((APP_PATH).resolve().parent).resolve()
# APP_PATH = (Path('index.py').resolve())
# data_path = ((APP_PATH).resolve().parent / './data/').resolve()
