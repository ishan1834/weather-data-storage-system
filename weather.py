class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature


class DataStorage:
    def __init__(self, years, cities, sentinel=None):
        self.years = years
        self.cities = cities
        self.sentinel = sentinel
        self.year_to_idx = {y: i for i, y in enumerate(years)}
        self.city_to_idx = {c: i for i, c in enumerate(cities)}
        self.matrix = [[sentinel for _ in cities] for _ in years]
        self.sparse = {}

    def insert(self, record):
        year = int(record.date.split("/")[-1])
        city = record.city
        temp = record.temperature
        if year in self.year_to_idx and city in self.city_to_idx:
            i = self.year_to_idx[year]
            j = self.city_to_idx[city]
            self.matrix[i][j] = temp
        self.sparse[(year, city)] = temp

    def delete(self, city, date):
        year = int(date.split("/")[-1])
        if (year, city) in self.sparse:
            del self.sparse[(year, city)]
            i = self.year_to_idx.get(year)
            j = self.city_to_idx.get(city)
            if i is not None and j is not None:
                self.matrix[i][j] = self.sentinel
            return True
        return False

    def retrieve(self, city, year):
        if (year, city) in self.sparse:
            return self.sparse[(year, city)]
        return None

    def row_major_access(self):
        result = []
        for i, y in enumerate(self.years):
            for j, c in enumerate(self.cities):
                result.append((y, c, self.matrix[i][j]))
        return result

    def column_major_access(self):
        result = []
        for j, c in enumerate(self.cities):
            for i, y in enumerate(self.years):
                result.append((y, c, self.matrix[i][j]))
        return result

    def handle_sparse_data(self):
        total = len(self.years) * len(self.cities)
        filled = len(self.sparse)
        missing = total - filled
        return {"total": total, "filled": filled, "missing": missing}
