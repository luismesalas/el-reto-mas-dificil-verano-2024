import argparse
from enum import Enum

import pandas as pd


class ColorValue(Enum):
    """
    This Enum is to define the value of each color
    """
    PURPLE = 7
    BLUE = 6
    PINK = 5
    ORANGE = 4
    YELLOW = 3
    LIME = 2
    GREEN = 1


def read_input(file_path: str):
    """
    Reads a CSV file with two columns: sides, value. Then return a Pandas dataframe with its content.

    Parameters:
    file_path (str): Path to CSV file

    Returns:
    pandas.Dataframe: Containing shapes and its colors code
    """
    return pd.read_csv(file_path)


def compute_values(raw_df: pd.DataFrame):
    """
    Iterate over colors, creating a new dataframe with the total weight and total value grouped by color

    Parameters:
    raw_df (str): Original dataframe containing shapes and colors

    Returns:
    pandas.Dataframe: Containing the total weight and total value for each color selection
    """
    result_df = pd.DataFrame(columns=['color', 'total_weight', 'total_value'])
    for color in ColorValue:
        color_df = raw_df[raw_df['color'] == color.value]
        result_df = result_df._append({'color': color.name, 'total_weight': color_df['lados'].sum(),
                                       'total_value': len(color_df.index) * color.value}, ignore_index=True)
    return result_df


def determine_max_benefit(groups_df: pd.DataFrame, capacity: int):
    """
    Filter all classes that exceed the total capacity, then sort the dataframe by value and returns a message with the
    most profitable class

    Parameters:
    groups_df (pandas.Dataframe): Dataframe with the total weight and total value for each colour selection

    Returns:
    str: Message with which class is the most profitable and what is its total weight and profit
    """
    filtered_by_capacity = groups_df[groups_df['total_weight'] <= capacity]
    sorted_df = filtered_by_capacity.sort_values('total_value', ascending=False)
    return (f"The most profitable class is: {sorted_df.head(1)['color'].values[0]} with a weight of "
            f"{sorted_df.head(1)['total_weight'].values[0]} and a benefit of "
            f"{sorted_df.head(1)['total_value'].values[0]} units!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='El reto más difícil: verano 2024. Semana 2, LOS ESTIBADORES. Cree un '
                                                 'CSV que contenga las siguientes columnas: lados, color. Los lados'
                                                 'representan el peso y el valor se toma en función de los siguientes '
                                                 'colores, ordenados de menor a mayor: verde, lima, amarillo, naranja, '
                                                 'rosa, azul, morado. Pase dicho CSV y la capacidad del barco para '
                                                 'obtener la carga más valiosa por pantalla.',
                                     epilog='luismesalas@gmail.com')
    parser.add_argument("--csv", "-c", type=str, required=True, help="Ruta al fichero CSV con las formas "
                                                                     "y colores")
    parser.add_argument("--almacenamiento", "-a", type=int, required=True, help="Clave de cifrado (desplazamiento)")

    args = parser.parse_args()

    input_df = read_input(args.csv)
    grouped_by_color_df = compute_values(input_df)
    print(determine_max_benefit(grouped_by_color_df, args.almacenamiento))
