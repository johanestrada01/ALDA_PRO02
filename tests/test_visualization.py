import pandas as pd
from src.visualization import plot_year_histogram, plot_brand_counts, plot_model_trend

def test_plot_year_histogram():
    df = pd.DataFrame({"year": [2000, 2005, 2010]})
    fig = plot_year_histogram(df)
    assert fig is not None

def test_plot_brand_counts():
    df = pd.DataFrame({"brand": ["Toyota", "Ford", "Toyota"]})
    fig = plot_brand_counts(df)
    assert fig is not None

def test_plot_model_trend():
    df = pd.DataFrame({"model": ["X", "X", "Y"], "year": [2000, 2001, 2000]})
    fig = plot_model_trend(df, "X")
    assert fig is not None
