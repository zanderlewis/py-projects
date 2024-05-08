# Requirements: pandas, matplotlib
# Difficulty: VI

import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('cars.csv')

def visualize_data(df, x, y):
    plt.figure(figsize=(10,6))
    plt.scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs {x}')
    plt.show()

# Call the function
visualize_data(df, 'Horsepower', 'MPG')