import pandas as pd

def filter_by_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
    return df[df["year"] >= year]

def count_by_brand(df: pd.DataFrame) -> pd.Series:
    return df["brand"].value_counts()

def average_engine_size(df: pd.DataFrame) -> float:
    return df["engine_size"].str.replace("L", "").astype(float).mean()

def average_safety_rating(df: pd.DataFrame) -> float:
    return df["safety_rating"].str.extract("(\d)").astype(float).mean()[0]

def count_by_fuel_type(df: pd.DataFrame) -> pd.Series:
    return df["fuel_Type"].value_counts()

def count_accidents(df: pd.DataFrame) -> int:
    return df["accident_history"].astype(str).str.upper().eq("VERDADERO").sum()

def average_odometer_reading(df: pd.DataFrame) -> float:
    return df["odometer_reading"].astype(float).mean()

def most_common_vehicle_color(df: pd.DataFrame) -> str:
    return df["color"].mode()[0]

def average_market_value(df: pd.DataFrame) -> float:
    return pd.to_numeric(df["estimated_market_value"], errors="coerce").mean()

def percentage_with_gps(df: pd.DataFrame) -> float:
    return (df["gps_installed"].astype(int).sum() / len(df)) * 100
