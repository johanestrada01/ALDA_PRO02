import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(path)
        return df
    except Exception as e:
        raise RuntimeError(f"Error cargando datos: {e}")
