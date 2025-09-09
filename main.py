from weather_ds import WeatherRecord, DataStorage

years = [2023, 2024]
cities = ["Delhi", "Chennai", "Mumbai"]
ds = DataStorage(years, cities, sentinel=None)

r1 = WeatherRecord("01/01/2023", "Delhi", 23.4)
r2 = WeatherRecord("15/06/2023", "Chennai", 30.7)
r3 = WeatherRecord("12/05/2024", "Mumbai", 28.1)
r4 = WeatherRecord("02/02/2024", "Delhi", 18.9)

for r in [r1, r2, r3, r4]:
    ds.insert(r)

print("Row Major:")
print(ds.row_major_access())

print("Column Major:")
print(ds.column_major_access())

print("Retrieve Delhi 2023:", ds.retrieve("Delhi", 2023))

print("Sparse Summary:", ds.handle_sparse_data())

print("Delete Delhi 01/01/2023:", ds.delete("Delhi", "01/01/2023"))
print("Retrieve Delhi 2023 after delete:", ds.retrieve("Delhi", 2023))
