import pandas as pd

def filter_by_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
    return df[df["year"] >= year]

def count_by_brand(df: pd.DataFrame) -> pd.Series:
    return df['brand'].value_counts()
