import pandas as pd
from src.processing import filter_by_year, count_by_brand

def test_filter_by_year():
    df = pd.DataFrame({"year": [2000, 2010, 2020]})
    filtered = filter_by_year(df, 2010)
    assert all(filtered['year'] >= 2010)

def test_count_by_brand():
    df = pd.DataFrame({"brand": ["Toyota", "Ford", "Toyota"]})
    counts = count_by_brand(df)
    assert counts["Toyota"] == 2
