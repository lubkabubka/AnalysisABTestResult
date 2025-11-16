import pandas as pd
from pathlib import Path
from narwhals import read_csv
from sqlalchemy import create_engine
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "data" / "ab_data.csv"
table = read_csv(DB_PATH, backend="pandas",sep=",")