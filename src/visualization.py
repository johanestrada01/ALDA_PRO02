import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_year_distribution(df: pd.DataFrame):
    sns.histplot(df['year'].dropna(), bins=15, kde=True)
    plt.title("Distribución de años de fabricación")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de vehículos")

def plot_brand_counts(df: pd.DataFrame):
    top_brands = df['brand'].value_counts().nlargest(10)
    top_brands.plot(kind='bar')
    plt.title("Top 10 marcas de vehículos")
    plt.xlabel("Marca")
    plt.ylabel("Cantidad")

def plot_fuel_type_distribution(df: pd.DataFrame):
    df['fuel_Type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Distribución por tipo de combustible")
    plt.ylabel("")

def plot_transmission_distribution(df: pd.DataFrame):
    df['transmission_type'].value_counts().plot(kind='bar')
    plt.title("Distribución por tipo de transmisión")
    plt.xlabel("Tipo de transmisión")
    plt.ylabel("Cantidad")

def plot_market_value_distribution(df: pd.DataFrame):
    sns.boxplot(x=df['estimated_market_value'])
    plt.title("Distribución del valor estimado en el mercado")
    plt.xlabel("Valor estimado")

def plot_accident_by_brand(df: pd.DataFrame):
    df_acc = df[df['accident_history'] == True]
    top_brands = df_acc['brand'].value_counts().nlargest(10)
    top_brands.plot(kind='bar', color='red')
    plt.title("Top 10 marcas con más vehículos con historial de accidentes")
    plt.xlabel("Marca")
    plt.ylabel("Cantidad con accidentes")

def plot_vehicle_status(df: pd.DataFrame):
    df['vehicle_status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Distribución por estado del vehículo")
    plt.ylabel("")

def plot_odometer_vs_year(df: pd.DataFrame):
    sns.scatterplot(data=df, x='year', y='odometer_reading', alpha=0.5)
    plt.title("Relación entre año del vehículo y kilometraje")
    plt.xlabel("Año")
    plt.ylabel("Lectura del odómetro")

def plot_doors_distribution(df: pd.DataFrame):
    df['number_of_doors'].value_counts().sort_index().plot(kind='bar')
    plt.title("Distribución por número de puertas")
    plt.xlabel("Número de puertas")
    plt.ylabel("Cantidad de vehículos")

def plot_fuel_vs_transmission(df: pd.DataFrame):
    cross_tab = pd.crosstab(df['fuel_Type'], df['transmission_type'])
    cross_tab.plot(kind='bar', stacked=True)
    plt.title("Combustible vs Transmisión")
    plt.xlabel("Tipo de combustible")
    plt.ylabel("Cantidad")

def plot_year_distribution(df: pd.DataFrame):
    df['year'].value_counts().sort_index().plot(kind='bar')
    plt.title("Distribución por año de fabricación")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de vehículos")
