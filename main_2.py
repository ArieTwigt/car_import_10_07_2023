from custom_modules.import_functions import import_car_brand
from custom_modules.export_functions import export_cars_brand

selected_brand = input("Select a brand:\n")

car_data = import_car_brand(selected_brand)
export_cars_brand(car_data, selected_brand)

pass