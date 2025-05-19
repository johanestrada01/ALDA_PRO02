import matplotlib.pyplot as plt
from src.parser import load_data
from src.visualization import (
    plot_year_distribution,
    plot_brand_counts,
    plot_fuel_type_distribution,
    plot_transmission_distribution,
    plot_market_value_distribution,
    plot_accident_by_brand,
    plot_vehicle_status,
    plot_odometer_vs_year,
    plot_fuel_vs_transmission,
    plot_doors_distribution
)

def main():
    # Ruta del archivo de datos
    data_path = "data/out_20000.xlsx"

    # Cargar los datos
    df = load_data(data_path)

    # Crear una figura nueva para cada gráfico
    plt.figure(); plot_year_distribution(df)
    plt.figure(); plot_brand_counts(df)
    plt.figure(); plot_fuel_type_distribution(df)
    plt.figure(); plot_transmission_distribution(df)
    plt.figure(); plot_market_value_distribution(df)
    plt.figure(); plot_accident_by_brand(df)
    plt.figure(); plot_vehicle_status(df)
    plt.figure(); plot_doors_distribution(df)

    # Ajustar layout para evitar solapamientos
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
