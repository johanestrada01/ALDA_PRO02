# Proyecto de Parsing, Gráficas y Análisis de Datos

Este proyecto carga un dataset de vehículos, lo procesa y genera análisis visual.

## Estructura
- `src/`: Código fuente para parsing, procesamiento y visualización.
- `tests/`: Pruebas unitarias.
- `notebooks/`: Jupyter Notebook para análisis y presentación.
- `data/`: Carpeta para colocar tu archivo `out_20000.xlsx`.

## Instalación
```bash
pip install -r requirements.txt
```

## Uso
```python
from src.parser import load_data
from src.processing import filter_by_year
from src.visualization import plot_year_histogram

df = load_data("data/out_20000.xlsx")
df_filtered = filter_by_year(df, 2010)
fig = plot_year_histogram(df_filtered)
fig.show()
```

## Pruebas
```bash
pytest --cov=src
```
# ALDA_PRO02
