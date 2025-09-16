from weather import WeatherRecord, DataStorage

years = [2025, 2026]
cities = ["Delhi", "Chennai", "Mumbai"]
ds = DataStorage(years, cities, sentinel=None)

r1 = WeatherRecord("01/01/2025", "Delhi", 23.4)
r2 = WeatherRecord("15/06/2025", "Chennai", 30.7)
r3 = WeatherRecord("12/05/2025", "Mumbai", 28.1)
r4 = WeatherRecord("02/02/2025", "Delhi", 18.9)

for r in [r1, r2, r3, r4]:
    ds.insert(r)

print("Row Major:")
print(ds.row_major_access())

print("Column Major:")
print(ds.column_major_access())

print("Retrieve Delhi 2025:", ds.retrieve("Delhi", 2025))

print("Sparse Summary:", ds.handle_sparse_data())

print("Delete Delhi 01/01/2025:", ds.delete("Delhi", "01/01/2025"))
print("Retrieve Delhi 2025 after delete:", ds.retrieve("Delhi", 2025))
