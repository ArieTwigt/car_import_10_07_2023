import pandas as pd
import os


def export_cars_brand(data, brand):
    # Convert the list with cars to a DataFrame
    data_df = pd.DataFrame(data)

    # Only keep the columns specified in the list
    columns = ['merk', 'handelsbenaming', 'catalogusprijs', 'eerste_kleur']
    data_df_filtered = data_df[columns]

    # create the folder for the brand
    files_folders = os.listdir()

    # provide the name of the folder
    folder_name = f"export/{brand}"

    # check if the folder already exists
    if folder_name.lower() not in files_folders:
        print(f"Creating folder {folder_name}")
        os.mkdir(folder_name.lower())

    # define the path for the export
    file_path = f"{folder_name}/export_{brand}.csv"

    # export the DataFrame
    data_df_filtered.to_csv(file_path, sep=";", index=False)

    print(f"Finished exporting for brand {brand}")