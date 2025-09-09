# 🌤 Weather Data Storage System

## Project Overview

A Python-based **Weather Data Storage System** that organizes temperature records by **city** and **year** using **2D arrays** and **Abstract Data Types (ADTs)**. It supports insertion, deletion, retrieval, row-major/column-major traversal, and sparse data handling.

## Features

* Store weather records (date, city, temperature)
* Insert, delete, and retrieve records
* Row-major & column-major data access
* Sparse data handling with sentinel values and dictionary storage
* Memory-efficient storage for incomplete datasets

## Installation

* Requires **Python 3.x**
* No external libraries needed

## Usage

```python
from weather_ds import WeatherRecord, DataStorage

years = [2025, 2026]
cities = ["Gurgaon"]
ds = DataStorage(years, cities, sentinel=None)

r1 = WeatherRecord("01/06/2025", "Gurgaon", 34)
r2 = WeatherRecord("15/07/2026", "Gurgaon", 31)

ds.insert(r1)
ds.insert(r2)

print("Retrieve Gurgaon 2025:", ds.retrieve("Gurgaon", 2025))
print("Row-major:", ds.row_major_access())
print("Sparse summary:", ds.handle_sparse_data())
```

## Sample Output

```
Retrieve Gurgaon 2025: 34
Row-major: [(2025, 'Gurgaon', 34), (2026, 'Gurgaon', 31)]
Sparse summary: {'total': 2, 'filled': 2, 'missing': 0}
```

## Time and Space Complexity

| Operation        | Dense (2D Array) | Sparse (Dictionary) |
| ---------------- | ---------------- | ------------------- |
| Insert           | O(1)             | O(1)                |
| Delete           | O(1)             | O(1)                |
| Retrieve         | O(1)             | O(1)                |
| Row Traversal    | O(n × m)         | O(k)                |
| Column Traversal | O(n × m)         | O(k)                |

**Space Complexity:** Dense → O(n × m), Sparse → O(k)

## Project Structure

```
├── weather_ds.py   # ADT & DataStorage implementation
├── main.py         # Demo / Example usage
├── README.md       # Project description and report
└── report.docx     # Assignment report
```

## License

For academic purposes only under **Data Structures course ENCS205 / ENCA201**.
