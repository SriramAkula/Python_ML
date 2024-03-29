import csv

# Data to be written into the CSV file
data = [
    ["S. No.", "Names", "Years of Experience", "Domain", "Relevant Experience", "Income(USD)", "Marital Status", "Number of siblings", "dummy"],
    [1, "John", 8, "Automotive", 6.0, 20000.0, "Single", 3, 0.0],
    [2, "Jason", 5, "Entertainment", 4.0, 15000.0, "Married", 3, 0.0],
    [3, "Maria", 10, "Banking", 3.0, 18000.0, "Single", 3, 0.0],
    [4, "Jacob", 12, "Insurance", 10.0, 24000.0, "Single", 3, 0.0],
    [5, "Sarah", 15, "Logistics", 5.0, 8000.0, "Married", 3, 0.0],
    [6, "Angelina", 3, "Travel", 3.0, 9500.0, "Married", 3, 0.0],
    [7, "Krishna", 0, "NaN", "NaN", "NaN", "Single", 3, 0.0],
    [8, "Adam", 8, "Food", 5.0, 7500.0, "Single", 3, 0.0],
    [9, "Deepika", 15, "IT", 13.0, 19500.0, "Married", 3, 0.0],
    [10, "Alan", 2, "Space", 1.0, 12500.0, "Married", 3, 0.0]
]

# Specify the file name
csv_file = 'data.csv'

# Write data into the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'CSV file "{csv_file}" has been created successfully.')