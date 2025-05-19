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
from src.processing import (
    filter_by_year,
    count_by_brand,
    average_engine_size,
    average_safety_rating,
    count_by_fuel_type,
    count_accidents,
    average_odometer_reading,
    most_common_vehicle_color,
    average_market_value,
    percentage_with_gps
)

def main():
    data_path = "data/out_20000.xlsx"
    df = load_data(data_path)

    plt.figure(); plot_year_distribution(df)
    plt.figure(); plot_brand_counts(df)
    plt.figure(); plot_fuel_type_distribution(df)
    plt.figure(); plot_transmission_distribution(df)
    plt.figure(); plot_market_value_distribution(df)
    plt.figure(); plot_accident_by_brand(df)
    plt.figure(); plot_vehicle_status(df)
    plt.figure(); plot_doors_distribution(df)

    print("Cantidad de vehículos por marca:")
    print(count_by_brand(df))

    print("\nPromedio del tamaño del motor:")
    print(average_engine_size(df))

    print("\nPromedio del rating de seguridad:")
    print(average_safety_rating(df))

    print("\nCantidad de vehículos por tipo de combustible:")
    print(count_by_fuel_type(df))

    print("\nCantidad de vehículos con historial de accidentes:")
    print(count_accidents(df))

    print("\nPromedio del odómetro:")
    print(average_odometer_reading(df))

    print("\nColor más común:")
    print(most_common_vehicle_color(df))

    print("\nValor promedio estimado del mercado:")
    print(average_market_value(df))

    print("\nPorcentaje de vehículos con GPS:")
    print(percentage_with_gps(df))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
