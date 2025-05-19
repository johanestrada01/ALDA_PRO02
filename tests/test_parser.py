import pandas as pd
from src.parser import load_data

def test_load_data(tmp_path):
    df = pd.DataFrame({"a": [1, 2, 3]})
    file = tmp_path / "test.xlsx"
    df.to_excel(file, index=False)
    result = load_data(file)
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == ["a"]
