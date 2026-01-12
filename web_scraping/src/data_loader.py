import pandas as pd

def save_data(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False, encoding="utf-8-sig")

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8-sig")
