import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)
print(cars)